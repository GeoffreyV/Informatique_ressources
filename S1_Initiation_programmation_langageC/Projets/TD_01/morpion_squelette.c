int main(void) {

    int l_tab_jeu[9] = {1,0,0,0,2,0,1,0,2};

    int iBcl1 = 0, iBcl2 = 0, l_joueur = 0, l_cpt = 0;

    for(iBcl2 = 0 ; iBcl2 <3 ; iBcl2++){
        printf("\n+---+---+---+\n|");
        for(iBcl1 = 6-3*iBcl2 ; iBcl1<9-3*iBcl2;iBcl1++){
            printf(" %c |",(l_tab_jeu[iBcl1]==1)*'X' + (l_tab_jeu[iBcl1]==2)*'O' + (l_tab_jeu[iBcl1]==0)*32);
        }
    }
    printf("\n+---+---+---+\n");

    do{
        l_joueur = (l_cpt%2) + 1 ;
        printf("\n\nJoueur %i joue", l_joueur);
        l_cpt++;
    }while(1);

    return 0;
}
