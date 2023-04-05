#define DIRECTION 2
#define VALIDATION 3
String haut = "foward";   // si ce que tu envoies est égal à haut alors la led s'allume
String bas = "backward";  //  si ce que tu envoies est égal à bas alors la led s'allume
String stop = "stop";


boolean etat_1;
boolean etat_2;
boolean etat_3;
int vitesse = 100;
int aff_vitesse;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);          // initialisation du moniteur série
  pinMode(DIRECTION, OUTPUT);  // configuration des broches
  pinMode(VALIDATION, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  //Serial.println("Enter data:");
  while (Serial.available() == 0) {}   //wait for data available
  String dataT = Serial.readString();  //read until timeout
  dataT.trim();                        // remove any \r \n whitespace at the end of the String



  if (dataT == haut) {
    digitalWrite(DIRECTION, HIGH);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(VALIDATION, vitesse);
    aff_vitesse = map(vitesse, 0, 255, 0, 100);  // changement d'échelle pour l'affichage (0 à 100 %)
    Serial.print("La vitesse du moteur est egale a ");
    Serial.print(aff_vitesse);
    Serial.println(" %.");
    delay(1000);

    
  } else if (dataT == bas) {
    digitalWrite(DIRECTION, LOW);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(VALIDATION, vitesse);
    aff_vitesse = map(vitesse, 0, 255, 0, 100);  // changement d'échelle pour l'affichage (0 à 100 %)
    Serial.print("La vitesse du moteur est egale a ");
    Serial.print(aff_vitesse);
    Serial.println(" %.");
    delay(1000);
  

  } else if (dataT == stop) {
    
    digitalWrite(DIRECTION, LOW);  // pour faire tourner le moteur dans l'autre sens, mettre LOW à la place de HIGH
    analogWrite(VALIDATION, 0);
    aff_vitesse = map(vitesse, 0, 255, 0, 100);  // changement d'échelle pour l'affichage (0 à 100 %)
    Serial.print("La vitesse du moteur est egale a ");
    Serial.print(aff_vitesse);
    Serial.println(" %.");
    delay(1000);
  }
}