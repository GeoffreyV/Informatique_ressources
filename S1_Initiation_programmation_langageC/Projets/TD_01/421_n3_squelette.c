#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

static int points_combinaison(int a, int b, int c) {
    // Trier a <= b <= c
    if (a > b) { int t = a; a = b; b = t; }
    if (b > c) { int t = b; b = c; c = t; }
    if (a > b) { int t = a; a = b; b = t; }

    if (a == 1 && b == 2 && c == 4) return 21; // 421
    if (a == b && b == c) return c * 2;        // Triplette
    if (a == b || b == c) return (a == b) ? a : b; // Paire
    return 1; // Aucune
}

static void relance_interactive(int *d1, int *d2, int *d3) {
    string choix = get_string("Relancer quels dés ? (ex: 23, vide pour aucun) ");
    if (choix == NULL) return;
    for (int i = 0; choix[i] != '\0'; i++) {
        if (choix[i] == '1') *d1 = rand() % 6 + 1;
        else if (choix[i] == '2') *d2 = rand() % 6 + 1;
        else if (choix[i] == '3') *d3 = rand() % 6 + 1;
    }
}

int main(void) {
    int points[2] = {30, 30};
    int premier = 0; // Joueur qui commence la manche
    srand(time(NULL));

    while (points[0] > 0 && points[1] > 0) {
        printf("\n=== Nouvelle manche (Joueur %d commence) ===\n", premier + 1);

        int nb_lancers_ref = 0; // nombre de lancers effectués par le premier joueur
        int score_manche[2] = {0, 0};

        for (int tour = 0; tour < 2; tour++) {
            int joueur = (tour == 0) ? premier : 1 - premier;
            printf("\nJoueur %d :\n", joueur + 1);

            int d1 = rand() % 6 + 1;
            int d2 = rand() % 6 + 1;
            int d3 = rand() % 6 + 1;
            printf("Lancer 1 -> [%d %d %d]\n", d1, d2, d3);

            int nb_lancers = 1;
            if (tour == 0) {
                nb_lancers = get_int("Nombre total de lancers (1..3) ? ");
                if (nb_lancers < 1) nb_lancers = 1;
                if (nb_lancers > 3) nb_lancers = 3;
                nb_lancers_ref = nb_lancers;
            } else {
                nb_lancers = nb_lancers_ref;
                printf("(Imposé) Nombre total de lancers : %d\n", nb_lancers);
            }

            for (int l = 2; l <= nb_lancers; l++) {
                relance_interactive(&d1, &d2, &d3);
                printf("Après relance -> [%d %d %d]\n", d1, d2, d3);
            }

            int pts = points_combinaison(d1, d2, d3);
            score_manche[joueur] = pts;
            printf("Combinaison -> %d points\n", pts);
        }

        if (score_manche[0] > score_manche[1]) {
            points[0] += score_manche[0];
            points[1] -= score_manche[0];
            premier = 0;
            printf("=> Joueur 1 remporte la manche (+%d)\n", score_manche[0]);
        } else if (score_manche[1] > score_manche[0]) {
            points[1] += score_manche[1];
            points[0] -= score_manche[1];
            premier = 1;
            printf("=> Joueur 2 remporte la manche (+%d)\n", score_manche[1]);
        } else {
            printf("=> Égalité : aucun transfert\n");
            // Le premier joueur reste le même en cas d'égalité
        }

        printf("Scores -> J1: %d | J2: %d\n", points[0], points[1]);
    }

    if (points[0] <= 0) printf("Victoire du Joueur 2 !\n");
    else printf("Victoire du Joueur 1 !\n");

    return 0;
}
