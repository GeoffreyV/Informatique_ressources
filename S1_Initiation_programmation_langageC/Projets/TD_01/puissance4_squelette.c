int main(void) {

    int l_tab_grille[6][6];
    int iBclX = 0, iBclY = 0, l_joueur = 0, l_cpt = 0;

    for(iBclX=0;iBclX<6;iBclX++){
        for(iBclY=0;iBclY<6;iBclY++){
            l_tab_grille[iBclX][iBclY] = 0;
            printf("%i ",l_tab_grille[iBclX][iBclY]);
        }
        printf("\n");
    }

    do{
        l_joueur = (l_cpt%2) + 1 ;
        printf("\n\nJoueur %i joue", l_joueur);
        l_cpt++;
    }while(1);

    return 0;
}
