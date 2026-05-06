int main(void) {
int tab_joueurs_points[2]; //Déclaration du tableau de point des 2 joueurs
int tab_jeu[6]; //Déclaration du tableau de jeu. Les 3 chiffres du tirage du joueur 1 seront rangés dans les 3 premières cases de ce tableau, les 3 chiffres du joueur 2 seront rangés dans les 3 suivantes.
bool joueur = 0;
int iBcl = 0 ;
char lettre = 0;

srand(time(NULL)); // Initialise le générateur aléatoire. Nécessite #include <time.h>

do{
    printf("Joueur %d joue :\n", joueur);

    //Boucle for qui lance 3 dés et mémorise dans le tableau de jeu et affiche :
    for(iBcl = 0;iBcl<3;iBcl++){
        tab_jeu[l_joueur * 3+iBcl] = rand(); //Utilisez % !!!
        printf("Dé %d de joueur %d = %d\n", iBcl+1, joueur, tab_jeu[joueur*3+iBcl]);
    }

    lettre = get_char("Appuyez sur une touche pour passer au joueur suivant. q pour sortir.\n");
    joueur = !joueur; //Pour passer au 2ème joueur
}while(lettre != 'q');

return 0;
} 