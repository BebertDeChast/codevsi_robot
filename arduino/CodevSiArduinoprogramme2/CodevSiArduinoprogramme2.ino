#include <Wire.h>
#include <avr/wdt.h>

void relancerProgramme() {
  wdt_enable(WDTO_15MS);
  while (1) {}
}


#define BRB_I2C_ADDR 0x42
#define BRB_ID_REG_ADD 0x00
#define BRB_POS_M0_REG_ADD 0x01
#define BRB_POS_M1_REG_ADD 0x05
#define BRB_SPE_M0_REG_ADD 0x09
#define BRB_SPE_M1_REG_ADD 0x0D
#define BRB_PERIOD_REG_ADD 0x11

char mess[16];


#define vitesseL 10    //  D2 vitesse
#define directionL 37  // INV  sens
#define BLANCL 39      // EN  on/off


#define vitesseR 11    //  D2 vitesse
#define directionR 36  // INV  sens
#define BLANCR 38      // EN  on/off

float rayonRoue = 4;  // 4cm

float errorL = 0;
float integrateurL = 0;


int puissanceL = 0;
int puissanceR = 0;

int speedR, speedL = 0;  //M0: gauche dans le sens de la marche, M1: droit
int period;

float speedLCalc, speedRCalc = 0;

byte flag = 0;

const int nbCommandes = 70;
const int tailleCommande = nbCommandes * 5 + 1;

void setup() {
  Serial.begin(9600);  // initialisation du moniteur série
  Wire.begin();
  pinMode(vitesseR, OUTPUT);  // configuration des broches
  pinMode(directionR, OUTPUT);
  pinMode(directionL, OUTPUT);  // configuration des broches
  pinMode(vitesseL, OUTPUT);
}

void loop() {

  // digitalWrite(BLANCR, LOW);
  // digitalWrite(directionR, HIGH);
  // analogWrite(vitesseR, 200);                   //vitesse du moteur droit


  // get_i2c(BRB_I2C_ADDR, BRB_SPE_M1_REG_ADD, (void *)&mess[0], sizeof(int));
  // memcpy(&speedL, (const void *)(&mess[0]), sizeof(int));
  // Serial.print(" et Speed M1: ");
  // Serial.println(speedL);

  while (Serial.available() != 0) {  //wait for data available

    delay(70);

    // Lecture de la chaîne de caractères
    String message = Serial.readStringUntil('\n');
    String commande[tailleCommande];
    message.trim();  // Suppression des caractères de fin de ligne

    // Déclaration du tableau de chaînes de caractères
    decoupage(commande, message, tailleCommande);  //String ListeCommande[36];  //max de 7 commandes     // 0: l ou r; // 1: SD; // 2: vitesseD // 3: SG // 4: vitesseG // 5: tempsD

    switch (message[0]) {

      case 'r':

        for (int i = 0; i < nbCommandes; i++) {
          errorL = 0;
          puissanceL = 0;

          long int t1 = millis();
          long int t2 = millis();
          long int t3 = millis();
          // Serial.print("i*5+4 : ");
          // Serial.println(commande[i * 5 + 4]);
          digitalWrite(BLANCR, HIGH);
          digitalWrite(BLANCL, HIGH);

          get_i2c(BRB_I2C_ADDR, BRB_PERIOD_REG_ADD, (void *)&mess[0], sizeof(int));
          memcpy(&period, (const void *)(&mess[0]), sizeof(int));

          while (abs(t2 - t1) < commande[i * 5 + 5].toInt()) {

            t3 = millis();

            get_i2c(BRB_I2C_ADDR, BRB_SPE_M0_REG_ADD, (void *)&mess[0], sizeof(int));
            memcpy(&speedL, (const void *)(&mess[0]), sizeof(int));

            get_i2c(BRB_I2C_ADDR, BRB_SPE_M1_REG_ADD, (void *)&mess[0], sizeof(int));
            memcpy(&speedR, (const void *)(&mess[0]), sizeof(int));
            //Serial.print("Speed M1: ");

            speedRCalc = vitesseLin(period, rayonRoue, speedR);
            speedLCalc = vitesseLin(period, rayonRoue, speedL);

            //Serial.print(" Speed M0: ");
            //Serial.print(abs(speedLCalc));
            //Serial.print(" et on veut : ");
            //Serial.print(abs(commande[i * 5 + 4].toInt() / 100));
            //Serial.print(" avec puissance :");
            //Serial.println(puissanceL);

            errorL = abs(speedLCalc) - abs(commande[i * 5 + 4].toInt() / 100) ;
            //Serial.print(" errorL: ");
            //Serial.print(errorL);


            integrateurL = integrateurL + errorL * (t3 - t2);
            if (integrateurL > 15000) {
              integrateurL =15000;
            }
            //Serial.print(" integrateurL ");
            //Serial.println(integrateurL);

            puissanceR = pid(speedRCalc, commande[i * 5 + 2].toInt() / 100, puissanceR, commande[i * 5 + 5].toInt());
            puissanceL = pid(speedLCalc, commande[i * 5 + 4].toInt() / 100, puissanceL, commande[i * 5 + 5].toInt());

            //puissanceL = pid2(integrateurL, errorL);

            digitalWrite(directionR, commande[i * 5 + 1].toInt());  //sens du moteur droit
            analogWrite(vitesseR, puissanceR);                      //vitesse du moteur droit

            digitalWrite(directionL, 1 - commande[i * 5 + 3].toInt());  //sens du moteur gauche
            analogWrite(vitesseL, puissanceL);                          //vitesse du moteur gauche

            // Serial.print("directionR : ");
            // Serial.print(commande[i * 5 + 1].toInt());
            // Serial.print(" et speedR : ");
            // Serial.print(puissanceR);
            // Serial.print(" et vitesse mesure : ");
            // Serial.println(speedL);

            t2 = millis();

            // URGENCE STOP
            // String test = Serial.readStringUntil('\n');
            // message.trim();  // Suppression des caractères de fin de ligne
            // if (test == 's') {
            //   Serial.write('o');
            //   relancerProgramme();
            // }
            float Kp = 5;
            float Ki = 3.5;
            Serial.print(abs(speedLCalc));
            Serial.print("/");
            Serial.print(speedRCalc);
            Serial.print("/");
            Serial.print((abs(t2 - t1)));
            Serial.print("/");
            Serial.print(integrateurL*Ki);
            Serial.print("/");
            Serial.println(errorL*Kp);
          }
          digitalWrite(BLANCR, LOW);
          digitalWrite(BLANCL, LOW);
          puissanceR = 0;
          puissanceL = 0;
        }

        break;

      case 't': Serial.write('k'); break;

      default: Serial.print("donnée.s inconnue.s"); break;
    }
  }
}