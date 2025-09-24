int largeur, hauteur;
    largeur = get_int("Entrer la largeur du rectangle :");
    hauteur = get_int("Entrer la hauteur du rectangle :");  
    for (int i=0; i<hauteur; i++){
        for (int j=0; j<largeur; j++){
            printf("*");
        }
        printf("\n");
    }
