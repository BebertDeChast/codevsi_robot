#define vitesseL 10    //  D2 vitesse
#define directionL 37  // INV  sens
#define BLANCL 39      // EN  on/off


#define vitesseR 11    //  D2 vitesse
#define directionR 36  // INV  sens
#define BLANCR 38      // EN  on/off


String forL = "forward left";    // le moteur tourne dans un sens dans cette configuration
String backL = "backward left";  //  le moteur tourne dans l'autre sens
String stopL = "stop left";      //  le moteur s'arrète
String fastL = "fast left";      //  le moteur accélère
String slowL = "slow left";      //  le moteur ralentit

String forR = "forward right";    // le moteur tourne dans un sens dans cette configuration
String backR = "backward right";  //  le moteur tourne dans l'autre sens
String stopR = "stop right";      //  le moteur s'arrète
String fastR = "fast right";      //  le moteur accélère
String slowR = "slow right";      //  le moteur ralentit


String test = "t";  //  variable de test


int speedL = 60;
int speedR = 100;
int aff_vitesse;
bool led = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);         // initialisation du moniteur série
  pinMode(vitesseL, OUTPUT);  // configuration des broches
  pinMode(directionL, OUTPUT);
  pinMode(BLANCL, INPUT);
  pinMode(vitesseR, OUTPUT);  // configuration des broches
  pinMode(directionR, OUTPUT);
  pinMode(BLANCR, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  //Serial.println("Enter data:");
  while (Serial.available() == 0) {}   //wait for data available
  String dataT = Serial.readString();  //read until timeout
  dataT.trim();                        // remove any \r \n whitespace at the end of the String

  if (dataT == test) {
    Serial.write("k\n");  // le code de lecture a besoin des "\n" pour savoir que le msg est fini
  }




//commande du moteur gauche


  else if (dataT == forL) {

    digitalWrite(BLANCL, HIGH);
    digitalWrite(directionL, LOW);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(vitesseL, speedL);

    delay(1000);


  } else if (dataT == backL) {

    digitalWrite(BLANCL, HIGH);
    digitalWrite(directionL, HIGH);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(vitesseL, speedL);

    delay(1000);


  } else if (dataT == stopL) {
    Serial.write("Left stop\n");
    digitalWrite(directionL, LOW);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(vitesseL, 0);

    delay(1000);

  } else if (dataT == fastL) {


    speedL = speedL + 30;
    analogWrite(vitesseL, speedL);


    delay(1000);
  } else if (dataT == slowL) {


    speedL = speedL - 30;
    analogWrite(vitesseL, speedL);
    delay(1000);
  }

  //commandes du moteur droit


  else if (dataT == forR) {

    digitalWrite(BLANCR, HIGH);    
    digitalWrite(directionR, HIGH);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(vitesseR, speedR);

    delay(1000);


  } else if (dataT == backR) {

    digitalWrite(BLANCR, HIGH);
    digitalWrite(directionR, LOW);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(vitesseR, speedR);

    delay(1000);


  } else if (dataT == stopR) {
    digitalWrite(directionR, LOW);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(vitesseR, 0);

    delay(1000);

  } else if (dataT == fastR) {



    speedR = speedR + 30;
    analogWrite(vitesseR, speedR);


    delay(1000);
  } else if (dataT == slowR) {



    speedL = speedL - 30;
    analogWrite(vitesseR, speedR);


    delay(1000);
  }





  else {
    Serial.write("error\n");
  }
}