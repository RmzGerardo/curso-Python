#include <stdio.h>

int main (){
    int i, j;
    i = 9;

    while (i > 0) {
        j = 0;
        if (j <= 0)
            printf("%d", i);

        while (j < i * 2) {
            printf("%d", i);
            j++;
        }

        i--;
        printf("\nssd");
    }
    return 0;
}