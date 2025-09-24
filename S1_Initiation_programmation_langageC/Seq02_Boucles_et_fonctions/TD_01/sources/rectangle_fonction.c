
#include <stdio.h>
#include <cs50.h>

void dessiner_ligne(int longueur);

void main(void){
    int largeur, hauteur;
    largeur = get_int("Entrer la largeur du rectangle :");
    hauteur = get_int("Entrer la hauteur du rectangle :");  
    for (int i=0; i<hauteur; i++){
        dessiner_ligne(largeur);
    }
    return 0;
}

void dessiner_ligne(int longueur){
    for (int i=0; i<longueur; i++){
        printf("*");
    }
    printf("\n");
}