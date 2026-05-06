int main(void) {
    char l_tab_jeuCorrect[50]; // Déclaration du tableau de jeu
    char l_tab_joueur[50];     // Déclaration du tableau du joueur pour la saisie
    int l_nbrCoup = 0, l_joueur = 0, iBcl = 0;

    srand(time(NULL)); // Initialise le générateur aléatoire. Nécessite #include <time.h>

    // On impose une seule boucle pour les 2 joueurs (même code) :
    do {
        printf("Joueur %d joue\n", l_joueur);

        l_tab_jeuCorrect[l_nbrCoup] = get_char("Quelle lettre ?");

        printf("Le tableau est : \n");
        for (iBcl = 0; iBcl <= l_nbrCoup; iBcl++) {
            printf("%c ", l_tab_jeuCorrect[iBcl]);
        }
        printf("\n\n");

        l_joueur = !l_joueur; // Pour passer au 2ème joueur
        l_nbrCoup++;

    } while (1); // Boucle infinie

    return 0;
}
