void printSquareColor(int x_code);

int main(void) {

    int iBcl;
    printf("\n");

    for(iBcl = 1;iBcl<=4;iBcl++){
        printSquareColor(iBcl);
        printf(" ");
    }
    return 0;
}

void printSquareColor(int x_code){

    switch(x_code){

        case 0 :
            printf("\033[40m  \033[0m");
        break;

        case 1 :
            printf("\033[41m  \033[0m");
        break;

        case 2 :
            printf("\033[42m  \033[0m");
        break;

        case 3 :
            printf("\033[44m  \033[0m");
        break;
    }
}
