void setup() {
  Serial.begin(9600);
  pinMode(52,OUTPUT);
}

void loop() {
  
  while (Serial.available() == 0) {}   //wait for data available
  String mode = Serial.readStringUntil('/');  //read until timeout sous forme : l/D.vitesse(%).temps(ms)/G.vitesse(%).temps(ms) ou r/D.vitesse(%).temps(ms)/G.vitesse(%).temps(ms) pour remote
  
  if (mode[0] == 't'){
    digitalWrite(52, HIGH);
    Serial.write('k');
  }
  
  int vitesseD = Serial.readStringUntil('.').toInt();
  int tempsD = Serial.readStringUntil('/').toInt();

  int vitesseG = Serial.readStringUntil('.').toInt();
  int tempsG = Serial.readStringUntil('.').toInt();
  mode.trim(); // remove any \r \n whitespace at the end of the String

  
}
