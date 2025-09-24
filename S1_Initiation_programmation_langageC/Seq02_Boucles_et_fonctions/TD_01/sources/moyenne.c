void main(void){
    int nombre_reels;
    double somme, moyenne, temp;

    somme = 0;
    nombre_reels = get_double("De combien de nombres souhaitez-vous obtenir la moyenne ?");

    for (int i=0; i<nombre_reels; i++){
        temp = get_int("Entrer le nombre (%i/%i)",i,nombre_reels);
        somme += temp;
    }
    moyenne = somme / nombre_reels;
    printf("La moyenne de ces %i nombres est de %lf.", moyenne);
    return 0;
}