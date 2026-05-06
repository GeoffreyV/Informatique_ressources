int main(void) {
    // Tableau officiel (2x pour 1..10, puis 25, 50, 75, 100)
    int l_tab_nombres[24] = {
        1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100
    };

    // Les 6 nombres tirés
    int l_tab_jeu[6] = {0};

    srand(time(NULL)); // Initialise le générateur aléatoire (une seule fois)

    // --- Tirage naf (Niv.1) :  améliorer  sans remise  au Niv.2 ---
    for (int i = 0; i < 6; i++) {
        int idx = rand(); // utilisez % pour borner
        l_tab_jeu[i] = l_tab_nombres[idx];
        printf("Tirage %d = %d\n", i + 1, l_tab_jeu[i]);
    }

    // --- Cible dans [100..999] (corriger la borne) ---
    int cible = rand(); // utilisez % pour borner dans [100..999]
    printf("Cible %d\n", cible);

    // --- Chrono de 60 s (tolérance 3 s en test) ---
    // Astuce : l_start = time(NULL); puis boucle jusqu'à (time(NULL)-l_start) >= 60

    return 0;
}
