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
        digitalWrite(BLANCR, HIGH);
        digitalWrite(BLANCL, HIGH);
        for (int i = 0; i < nbCommandes; i++) {

          long int t1 = millis();
          long int t2 = millis();
          // Serial.print("i*5+4 : ");
          // Serial.println(commande[i * 5 + 4]);
          

          

          while (abs(t2 - t1) < commande[i * 5 + 5].toInt()) {

            get_i2c(BRB_I2C_ADDR, BRB_SPE_M0_REG_ADD, (void *)&mess[0], sizeof(int));
            memcpy(&speedL, (const void *)(&mess[0]), sizeof(int));

            get_i2c(BRB_I2C_ADDR, BRB_SPE_M1_REG_ADD, (void *)&mess[0], sizeof(int));
            memcpy(&speedR, (const void *)(&mess[0]), sizeof(int));
            //Serial.print("Speed M1: ");
            
            speedRCalc = vitesseLin( rayonRoue, speedR);
            speedLCalc = vitesseLin( rayonRoue, speedL);

            Serial.print(" Speed M0: ");
            Serial.print(abs(speedLCalc));
            Serial.print(" et on veut : ");
            Serial.print(abs(commande[i * 5 + 4].toInt()/100));
            Serial.print(" avec puissance :");
            Serial.println(puissanceL);


            puissanceR = pid(speedRCalc, commande[i * 5 + 2].toInt()/100, puissanceR, commande[i * 5 + 5].toInt());
            puissanceL = pid(speedLCalc, commande[i * 5 + 4].toInt()/100, puissanceL, commande[i * 5 + 5].toInt());


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
          }
          
          puissanceR = 0;
          puissanceL = 0;
        }
        digitalWrite(BLANCR, LOW);
          digitalWrite(BLANCL, LOW);
        break;

      case 't': Serial.write('k'); break;

      default: Serial.print("donnée.s inconnue.s"); break;
    }
  }
  
}