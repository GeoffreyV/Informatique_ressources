int main(void)
{
    string l_mot;
    int iBcl = 0;

    l_mot = get_string("Entrer le mot \n");
    do{
        printf("%c\n",l_mot[iBcl]);
        iBcl++;
    }while(l_mot[iBcl] != 0);
}
