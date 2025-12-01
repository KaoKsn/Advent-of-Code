#include <stdio.h>
#include <stdlib.h>

#define CLK 100

// Count the number of times the dial finds 0 (even during rotations)
void decoder(char *val, int *prev, int *n) {
    char op = val[0];
    int rot = atoi(val + 1);
    if (op == 'L'){
        // To avoid n+=1 when prev is 0 then you don't need to count being in 0<initially>
        if (*prev == 0)
             *prev = 100;

        *n += (rot + (CLK - *prev)) / CLK;
        // If prev = 5 and rot = 10, -5 is the modulo in C.
        *prev = (*prev - rot) % CLK;
        if (*prev < 0)
            *prev += CLK;
        /** If prev = 0 and rot = 300, fine. **/
    } else {
        // rot + prev / CLK -> total times 0 is encountered (including currently pointing to 0)
        *n += (rot + *prev) / CLK, *prev = (*prev + rot) % CLK;
    }
    return;
}

int main(void) 
{
    int n = 0;
    int prev = 50;

    FILE *fptr = fopen("input.txt", "r");
    if (fptr == NULL)
      return 1;

    char buffer[10];

    while (fgets(buffer, 10, fptr) != NULL){
        decoder(buffer, &prev, &n);
    }
    printf("Password: %d\n" , n);
    fclose(fptr);
    return 0;
}
