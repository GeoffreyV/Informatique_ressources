#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

static int points_combinaison(int a, int b, int c) {
    // Trier a <= b <= c (tri simple à 3 éléments)
    if (a > b) { int t = a; a = b; b = t; }
    if (b > c) { int t = b; b = c; c = t; }
    if (a > b) { int t = a; a = b; b = t; }

    // 421 spécial
    if (a == 1 && b == 2 && c == 4) return 21;

    // Triplette
    if (a == b && b == c) return c * 2;

    // Paire
    if (a == b || b == c) {
        int val = (a == b) ? a : b;
        return val;
    }

    // Aucune combinaison
    return 1;
}

int main(void) {
    int points[2] = {30, 30};
    int joueur = 0; // 0 ou 1
    char cont = 0;

    srand(time(NULL));

    do {
        printf("\n=== Manche ===\n");

        int score_manche[2] = {0, 0};

        for (int tour = 0; tour < 2; tour++) {
            printf("\nJoueur %d :\n", joueur + 1);

            int nb_lancers = get_int("Nombre de lancers (1..3) ? ");
            if (nb_lancers < 1) nb_lancers = 1;
            if (nb_lancers > 3) nb_lancers = 3;

            int d1=0,d2=0,d3=0;
            for (int l = 1; l <= nb_lancers; l++) {
                d1 = rand() % 6 + 1;
                d2 = rand() % 6 + 1;
                d3 = rand() % 6 + 1;
                printf("Lancer %d -> [%d %d %d]\n", l, d1, d2, d3);
            }
            int pts = points_combinaison(d1,d2,d3);
            score_manche[joueur] = pts;
            printf("Combinaison -> %d points\n", pts);

            joueur = 1 - joueur;
        }

        // Déterminer gagnant de la manche (égalité -> pas de transfert)
        if (score_manche[0] > score_manche[1]) {
            points[0] += score_manche[0];
            points[1] -= score_manche[0];
            printf("=> Joueur 1 remporte la manche (+%d)\n", score_manche[0]);
        } else if (score_manche[1] > score_manche[0]) {
            points[1] += score_manche[1];
            points[0] -= score_manche[1];
            printf("=> Joueur 2 remporte la manche (+%d)\n", score_manche[1]);
        } else {
            printf("=> Égalité : aucun transfert\n");
        }

        printf("Scores -> J1: %d | J2: %d\n", points[0], points[1]);

        cont = get_char("Continuer ? (o/n) ");
    } while (cont != 'n' && points[0] > 0 && points[1] > 0);

    if (points[0] <= 0) printf("Victoire du Joueur 2 !\n");
    else if (points[1] <= 0) printf("Victoire du Joueur 1 !\n");

    return 0;
}
