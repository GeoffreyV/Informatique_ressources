#include <stdio.h>
#include <cs50.h>
int main(void) {
    int n;
    n = get_int("Entrer un nombre n");
    int fact = 1;
    while (n > 0) {
        fact *= n;
        n--;
    }
    printf("%d\n", fact);
    return 0;
}
