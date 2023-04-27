#define DIRECTION 2
#define VALIDATION 3
#define INCR3 4
#define INCR4 5



String haut = "forward";   // le moteur tourne dans un sens dans cette configuration
String bas = "backward";  //  le moteur tourne dans l'autre sens
String stop = "stop";     //  le moteur s'arrète
String fast = "fast";     //  le moteur accélère
String slow = "slow";     //  le moteur ralentit
String test = "t";        //  variable de test


int vitesse = 100;
int aff_vitesse;
bool led = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);          // initialisation du moniteur série
  pinMode(DIRECTION, OUTPUT);  // configuration des broches
  pinMode(VALIDATION, OUTPUT);
  pinMode(INCR3, INPUT);
  pinMode(INCR4, INPUT);
  pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  //Serial.println("Enter data:");
  while (Serial.available() == 0) {}   //wait for data available
  String dataT = Serial.readString();  //read until timeout
  dataT.trim();                        // remove any \r \n whitespace at the end of the String

  if  (dataT == test){
    Serial.write("k\n");               // le code de lecture a besoin des "\n" pour savoir que le msg est fini
    led = true;
    digitalWrite(13, led);

  }

  if  (dataT == "hello"){
    Serial.write("there");

  }
  
  else if (dataT == haut) {
    Serial.write("going forward\n");    
    led = false;
    digitalWrite(13, led);
    digitalWrite(DIRECTION, HIGH);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(VALIDATION, vitesse);
    aff_vitesse = map(vitesse, 0, 255, 0, 100);  // changement d'échelle pour l'affichage (0 à 100 %)

    delay(1000);

    
  } else if (dataT == bas) {
    Serial.write("going backward\n"); 
    led = false;
    digitalWrite(13, led);
    digitalWrite(DIRECTION, LOW);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(VALIDATION, vitesse);
    aff_vitesse = map(vitesse, 0, 255, 0, 100);  // changement d'échelle pour l'affichage (0 à 100 %)

    delay(1000);
  

  } else if (dataT == stop) {
    Serial.write("stop\n"); 
    led = false;
    digitalWrite(13, led);
    digitalWrite(DIRECTION, LOW);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(VALIDATION, 0);
    aff_vitesse = map(vitesse, 0, 255, 0, 100);  // changement d'échelle pour l'affichage (0 à 100 %)

    delay(1000);
    
  } else if (dataT == fast) {
    Serial.write("going faster\n"); 
    led = false;
    digitalWrite(13, led);
    vitesse = vitesse + 10;
    analogWrite(VALIDATION, vitesse);
    aff_vitesse = map(vitesse, 0, 255, 0, 100);  // changement d'échelle pour l'affichage (0 à 100 %)

    delay(1000);
  } else if (dataT == slow) {
    Serial.write("going slower\n"); 
    led = false;
    digitalWrite(13, led);
    vitesse = vitesse - 10;
    analogWrite(VALIDATION, vitesse);
    aff_vitesse = map(vitesse, 0, 255, 0, 100);  // changement d'échelle pour l'affichage (0 à 100 %)

    delay(1000);
  }

  
}