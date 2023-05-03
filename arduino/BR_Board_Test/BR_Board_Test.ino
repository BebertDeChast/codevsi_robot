#include <Wire.h>

#define BRB_I2C_ADDR 0x42
#define BRB_ID_REG_ADD     0x00
#define BRB_POS_M0_REG_ADD  0x01
#define BRB_POS_M1_REG_ADD  0x05
#define BRB_SPE_M0_REG_ADD  0x09
#define BRB_SPE_M1_REG_ADD  0x0D
#define BRB_PERIOD_REG_ADD  0x11

byte flag = 0;

void setup()
{
  Wire.begin();        
  Serial.begin(9600);  
}

void loop()
{
  char mess[16];
  int pos0, pos1;
  int spe0, spe1;
  int period;
  
  get_i2c(BRB_I2C_ADDR, BRB_ID_REG_ADD, (void *) &mess[0], sizeof(byte));
  Serial.print("Device ID: ");
  Serial.print("0x");
  Serial.println(mess[0], HEX);
  // read examples:
  get_i2c(BRB_I2C_ADDR, BRB_POS_M0_REG_ADD, (void *) &mess[0], sizeof(int));
  memcpy(&pos0, (const void*)(&mess[0]), sizeof(int));
  Serial.print("Position M0: ");
  Serial.println(pos0);
  get_i2c(BRB_I2C_ADDR, BRB_POS_M1_REG_ADD, (void *) &mess[0], sizeof(int));
  memcpy(&pos1, (const void*)(&mess[0]), sizeof(int));
  Serial.print("Position M1: ");
  Serial.println(pos1);
  get_i2c(BRB_I2C_ADDR, BRB_SPE_M0_REG_ADD, (void *) &mess[0], sizeof(int));
  memcpy(&spe0, (const void*)(&mess[0]), sizeof(int));
  Serial.print("Speed M0: ");
  Serial.println(spe0);
  get_i2c(BRB_I2C_ADDR, BRB_SPE_M1_REG_ADD, (void *) &mess[0], sizeof(int));
  memcpy(&spe1, (const void*)(&mess[0]), sizeof(int));
  Serial.print("Speed M1: ");
  Serial.println(spe1);
  get_i2c(BRB_I2C_ADDR, BRB_PERIOD_REG_ADD, (void *) &mess[0], sizeof(int));
  memcpy(&period, (const void*)(&mess[0]), sizeof(int));
  Serial.print("Period (");
  Serial.print(flag);
  Serial.print("): ");
  Serial.println(period);

  // write examples:
  if (flag == 1)
  {
    period = 5000;
    flag = 0;
  }
  else
  {
    period = 2000;
    flag = 1;
  }
  memcpy(&mess[0], (const void*)(&period),sizeof(int));
  set_i2c(BRB_I2C_ADDR, BRB_PERIOD_REG_ADD, (void *) (&mess[0]), sizeof(int));

  delay(500);
}

byte get_i2c(byte sad, byte sub, void * mess, byte len)
{
  byte * buff;
  byte i = 0;
  byte ret;
  buff = (byte *)(mess);
  Wire.beginTransmission(sad);
  Wire.write(sub); 
  Wire.endTransmission(sad); 
  Wire.requestFrom(sad,len);
  i = 0;   
  while (Wire.available())
  {
    buff[i] = Wire.read();
    i++;
  }
  return i;
}
void set_i2c(byte sad, byte sub, void * mess, byte len)
{
  byte * buff;
  buff = (byte *)(mess);
  Wire.beginTransmission(sad);
  Wire.write(sub); 
  Wire.write(&buff[0],len);
  Wire.endTransmission(sad);
}
