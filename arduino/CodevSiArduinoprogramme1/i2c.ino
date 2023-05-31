byte get_i2c(byte sad, byte sub, void *mess, byte len) {
  byte *buff;
  byte i = 0;
  byte ret;
  buff = (byte *)(mess);
  Wire.beginTransmission(sad);
  Wire.write(sub);
  Wire.endTransmission(sad);
  Wire.requestFrom(sad, len);
  i = 0;
  while (Wire.available()) {
    buff[i] = Wire.read();
    i++;
  }
  return i;
}

void set_i2c(byte sad, byte sub, void *mess, byte len) {
  byte *buff;
  buff = (byte *)(mess);
  Wire.beginTransmission(sad);
  Wire.write(sub);
  Wire.write(&buff[0], len);
  Wire.endTransmission(sad);
}