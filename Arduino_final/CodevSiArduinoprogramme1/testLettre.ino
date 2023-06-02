bool testLettre(char lettre) {
  bool etat;  // L'état correspondant à la lettre

  // Tableau de correspondance
  const char tableau[2][2] = {
    { 'H', 'L' },
    { true, false }
  };

  // Vérifie si la lettre correspond à un état true ou false
  for (int i = 0; i < 2; i++) {
    if (tableau[0][i] == lettre) {
      etat = tableau[1][i];
      break;
    }
  }

  return etat;
}