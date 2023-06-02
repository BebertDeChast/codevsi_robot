void decoupage(String ListeCommandes[], String text, int nbCommande) {

  //String ListeCommandes[nbCommande];

  // Découpage de la chaîne de caractères
  int pos = 0;
  int i = 0;
  while ((pos = text.indexOf("/")) != -1 && i < nbCommande - 1) {
    ListeCommandes[i] = text.substring(0, pos);
    text.remove(0, pos + 1);
    i++;
  }
  ListeCommandes[i] = text;  // Ajout du dernier élément au tableau
}