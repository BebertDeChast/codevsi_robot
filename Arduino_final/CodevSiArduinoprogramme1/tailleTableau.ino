int tailleTableau(int tableau[]) {
  int i = 0;
  while (tableau[i] != NULL) {  // boucle jusqu'à ce qu'on trouve la valeur NULL
    i++;
  }
  return i;
}