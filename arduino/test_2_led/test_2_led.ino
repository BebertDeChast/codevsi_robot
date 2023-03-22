String red = "red"; // si ce que tu envoies est égal à haut alors la led s'allume
String bas = "black"; //  si ce que tu envoies est égal à bas alors la led s'allume
String green = "green";
String orange =  "orange";

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(52,OUTPUT);
  pinMode(53,OUTPUT);
}

void loop() {
  
  //Serial.println("Enter data:");
  while (Serial.available() == 0) {}   //wait for data available
  String dataT = Serial.readString();  //read until timeout
  dataT.trim();                        // remove any \r \n whitespace at the end of the String
  
  if (dataT == red) { 
    digitalWrite(13, HIGH);
    Serial.write("red\n");
  }

  if (dataT == orange) { 
    digitalWrite(52, HIGH);
    Serial.write("orange\n");
  }

  if (dataT == green) { 
    digitalWrite(53, HIGH);
    Serial.write("green\n");
  }

  if (dataT == bas) {
digitalWrite(13,LOW);
digitalWrite(52,LOW);  
digitalWrite(53,LOW); 
Serial.write("black\n");  

  }
}
