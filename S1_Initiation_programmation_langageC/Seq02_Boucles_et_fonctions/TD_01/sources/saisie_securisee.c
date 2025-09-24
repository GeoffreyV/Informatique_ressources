int entier_saisi;
    do {
        entier_saisi = get_int("Entrer un entier positif :");
    } while (entier_saisi < 0);
    printf("Vous avez saisi %i.", entier_saisi);