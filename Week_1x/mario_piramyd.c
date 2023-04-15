#include <stdio.h>

int main() {
    int height;
    int i, j;

    do {
        printf("Enter the height of the pyramid (between 1 and 8): ");
        scanf("%d", &height);
    } while (height < 1 || height > 8);

    for (i = 1; i <= height; i++) {
        // Print spaces for left half of pyramid
        for (j = i; j < height; j++) {
            printf(" ");
        }
        // Print # for left half of pyramid
        for (j = 1; j <= i; j++) {
            printf("#");
        }
            printf(" ");
        // Print # for right half of pyramid
        for (j = 1; j <= i; j++) {
            printf("#");
        }
        printf("\n");
    }

    return 0;
}
