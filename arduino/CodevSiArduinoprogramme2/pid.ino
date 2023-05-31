int pid(float current_speed, float aim_speed, int puissance, int tempsMS) {

  int increment = 1 - 5 * (abs(current_speed) - abs(aim_speed)) / abs(aim_speed);
  // Serial.print("current_speed : ");
  // Serial.print(current_speed);
  // Serial.print(" et aim_speed : ");
  // Serial.print(aim_speed);
  // Serial.print(" et increment : ");
  // Serial.print(increment);

  if (abs(abs(aim_speed) - abs(current_speed)) > 0.5) {
    int puissanceCalc = puissance + increment * ((abs(aim_speed) - abs(current_speed)) / abs(abs(aim_speed) - abs(current_speed)));

    // Serial.print(" increment : ");
    // Serial.print(increment * ((abs(aim_speed) - abs(current_speed)) / abs(abs(aim_speed) - abs(current_speed))));
    // Serial.print(" et puissanceCalc : ");
    // Serial.println(puissanceCalc);

    if (puissanceCalc <= 255 && puissanceCalc >= 0) {
      return puissanceCalc;

    } else if (puissanceCalc > 255) {
      //puissanceCalc = 240;
      return 240;

    } else if (puissanceCalc < 0) {
      //puissanceCalc = 5;
      //Serial.println("return 0");
      return 0;
    }
  } else {
    return puissance;
  }
}
