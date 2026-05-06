#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// TODO : écrire ici la fonction factorisée
// Exemple : void duel(int numero_duel);

int main(void)
{
    int scoreJ1, scoreJ2;

    srand(time(NULL)); // initialisation du hasard

    printf("=== Duel 1 ===\n");
    scoreJ1 = rand() % 6 + 1;
    scoreJ2 = rand() % 6 + 1;
    printf("Joueur 1 lance le dé... %d !\n", scoreJ1);
    printf("Joueur 2 lance le dé... %d !\n", scoreJ2);
    if (scoreJ1 > scoreJ2)
        printf("-> Joueur 1 gagne ce duel !\n");
    else if (scoreJ2 > scoreJ1)
        printf("-> Joueur 2 gagne ce duel !\n");
    else
        printf("-> Égalité parfaite !\n");
    printf("-----------------------------\n");

    printf("=== Duel 2 ===\n");
    scoreJ1 = rand() % 6 + 1;
    scoreJ2 = rand() % 6 + 1;
    printf("Joueur 1 lance le dé... %d !\n", scoreJ1);
    printf("Joueur 2 lance le dé... %d !\n", scoreJ2);
    if (scoreJ1 > scoreJ2)
        printf("-> Joueur 1 gagne ce duel !\n");
    else if (scoreJ2 > scoreJ1)
        printf("-> Joueur 2 gagne ce duel !\n");
    else
        printf("-> Égalité parfaite !\n");
    printf("-----------------------------\n");

    printf("=== Duel 3 ===\n");
    scoreJ1 = rand() % 6 + 1;
    scoreJ2 = rand() % 6 + 1;
    printf("Joueur 1 lance le dé... %d !\n", scoreJ1);
    printf("Joueur 2 lance le dé... %d !\n", scoreJ2);
    if (scoreJ1 > scoreJ2)
        printf("-> Joueur 1 gagne ce duel !\n");
    else if (scoreJ2 > scoreJ1)
        printf("-> Joueur 2 gagne ce duel !\n");
    else
        printf("-> Égalité parfaite !\n");
    printf("-----------------------------\n");

    return 0;
}
