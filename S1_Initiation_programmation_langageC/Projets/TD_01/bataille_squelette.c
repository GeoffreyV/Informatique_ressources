int main(void){
    int l_tab_mer[6][6]; //Déclaration de la mer
    int iBclX, iBclY;

//Affichage de la première ligne de la grille (numéro de colonne) :

printf(" ");

for(iBclY=0;iBclY<6;iBclY++){
    printf("%i ",iBclY+1);
}

//Initialisation et affichage de la grille :

printf("\n");
for(iBclY=0;iBclY<6;iBclY++){ //Boucle des abscisses
    //Affichage de la lettre de la ligne :
    printf("%c ", iBclY+65);

    for(iBclX=0;iBclX<6;iBclX++){ //Boucle des ordonnées
    l_tab_mer[iBclY][iBclX] = 0; //Initialisation à 0
    printf("%i ",l_tab_mer[iBclY][iBclX]); //Affichage
    }

    printf("\n");
}

return 0;
}