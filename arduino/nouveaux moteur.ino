#define BLEU 11   //  D2
#define JAUNE 37  // INV
#define BLANC 39  // EN






void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);     // initialisation du moniteur série
  pinMode(BLEU, OUTPUT);  // configuration des broches
  pinMode(JAUNE, OUTPUT);
  pinMode(BLANC, INPUT);
}

String bleu_haut = "bleu_haut";
String bleu_bas = "bleu_bas";
String jaune_haut = "jaune_haut";
String jaune_bas = "jaune_bas";
String blanc_haut = "blanc_haut";
String blanc_bas = "blanc_bas";
int vitesse = 200;

void loop() {
  // put your main code here, to run repeatedly:

  //Serial.println("Enter data:");
  while (Serial.available() == 0) {}   //wait for data available
  String dataT = Serial.readString();  //read until timeout
  dataT.trim();                        // remove any \r \n whitespace at the end of the String



  

  if (dataT == bleu_haut) {
    analogWrite(BLEU, vitesse);
    Serial.write("bleu haut\n");
    delay(100);
  }

  else if (dataT == bleu_bas) {
    analogWrite(BLEU, 0);
    Serial.write("bleu bas\n");
    delay(100);
  }
  else if  (dataT == jaune_haut){
    digitalWrite(JAUNE, HIGH);
    Serial.write("jaune haut\n");
    delay(100);
  }
  else if  (dataT == jaune_bas){
    digitalWrite(JAUNE, LOW);
    Serial.write("jaune bas\n");
    delay(100);

  }
  else if  (dataT == blanc_haut){
    digitalWrite(BLANC, HIGH);
    Serial.write("blanc haut\n");
    delay(100);
  }
  else if  (dataT == blanc_bas){
    digitalWrite(BLANC, LOW);
    Serial.write("blanc bas\n");
    delay(100);
  }







}