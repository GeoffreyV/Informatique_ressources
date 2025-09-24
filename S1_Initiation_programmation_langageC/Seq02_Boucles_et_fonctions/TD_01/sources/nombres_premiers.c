int nombre = get_int("Entrer un entier naturel supérieur à 1 :");
    int est_premier = 1; // on suppose que le nombre est premier
    printf("Les diviseurs de %i sont : ", nombre);
    for (int i=2; i<=nombre/2; i++){
        if (nombre % i == 0){
            printf("%i ", i);
            est_premier = 0; // on a trouvé un diviseur, donc le nombre n'est pas premier
        }
    }
    if (est_premier){
        printf("\n%i est un nombre premier.", nombre);
    } else {
        printf("\n%i n'est pas un nombre premier.", nombre);
    }