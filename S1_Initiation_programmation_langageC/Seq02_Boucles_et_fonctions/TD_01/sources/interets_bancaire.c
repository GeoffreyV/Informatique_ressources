double montant_initial, taux_interet, montant_final;
    int duree_annees;

    montant_initial = get_double("Entrer le montant initial :");
    taux_interet = get_double("Entrer le taux d'interet (en %%):");
    duree_annees = get_int("Entrer la duree en annees :");

    montant_final = montant_initial;
    for (int i=0; i<duree_annees; i++){
        montant_final = montant_final * (1 + taux_interet / 100);
    }
    printf("Au bout de %i annees, un montant initial de %lf avec un taux d'interet de %lf%% devient %lf.", duree_annees, montant_initial, taux_interet, montant_final);
    return 0;


// Calcul du nombre d'années nécessaires pour doubler un investissement
    double montant_initial, taux_interet, montant_final;
    int duree_annees;   
    montant_initial = get_double("Entrer le montant initial :");
    taux_interet = get_double("Entrer le taux d'interet (en %%):"); 

    montant_final = montant_initial;
    duree_annees = 0;
    while (montant_final < 2 * montant_initial){
        montant_final = montant_final * (1 + taux_interet / 100);
        duree_annees++;
    }
    printf("Il faut %i annees pour doubler un montant initial de %lf avec un taux d'interet de %lf%%.", duree_annees, montant_initial, taux_interet);
    return 0;
