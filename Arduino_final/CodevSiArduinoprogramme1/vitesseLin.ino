float vitesseLin( float rayon, int speedMesure) {
  float omega, vitesse;  //vitesse en metre par seconde et omega en rad/s
  omega = 2 * PI * speedMesure / (2000e-6 * 2000 *36); //36 c'est le reducteur
  Serial.print(" vitesse de rotation : ");
  Serial.print(omega);
  return omega;
}