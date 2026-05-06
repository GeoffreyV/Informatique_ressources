int main(void) {

    char l_tab_rouleau[3][11] =     {{'L','7','C','B','L','C','L','L','C','L','B'},
                                     {'L','C','7','L','C','L','B','3','L','7','C'},
                                     {'L','B','L','C','L','7','C','L','B','C','L'}};

    int iBclX, iBclY;

    for(iBclX=0;iBclX<3;iBclX++){
        for(iBclY=0;iBclY<11;iBclY++){
            printf("%c ",l_tab_rouleau[iBclX][iBclY]);
        }
        printf("\n");
    }

    return 0;
}
