
//partie du code qui affiche toutes les combinaisons de poulets et de moutons
#define NBR_PATTES 74
    int nbr_poulets, nbr_moutons;
    for (nbr_poulets=0; nbr_poulets<=NBR_PATTES/2; nbr_poulets++){
        for (nbr_moutons=0; nbr_moutons<=NBR_PATTES/4; nbr_moutons++){
            if (2*nbr_poulets + 4*nbr_moutons == NBR_PATTES){
                printf("Il y peut rester %i poulets et %i moutons.\n", nbr_poulets, nbr_moutons);
            }
        }
    }