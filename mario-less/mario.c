#include <stdio.h>
#include <cs50.h>


// Prompt User
int main(void) {
   int height;
    do {
        height = get_int("Height: ");  // Prompt the user for height
    } while (height < 1 || height < 8);  // Reprompt the user if they hit 0 or less than 1

    printf("The entered height is %d\n", height);

}



