#include <stdio.h>
int main(void) {
    int choix;
    do {
        printf("Menu :\n");
        printf("1. Continuer\n");
        printf("0. Quitter\n");
        choix = get_int("Votre choix : ");
    } while (choix != 0);
    return 0;
}
