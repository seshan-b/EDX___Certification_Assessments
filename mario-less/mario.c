#include <stdio.h>
#include <cs50.h>


// Prompt User
int main(void)
{
   int height;
    do
    {
        height = get_int("Height: ");  // Prompt the user for height
    }
    while (height < 1 || height > 8);  // Reprompt the user if they hit 0 or less than 1

    // printf("The entered height is %d\n", height); // Hide this to pass test function
    // Loop through each level of the pyramid
    for (int row = 1; row <= height; row++)
    {
        // Print spaces before the hashes to align the pyramid to the right
        for (int space = 0; space < height - row; space++)
        {
            printf(" ");  // Print a space
        }
        // Print the hashes that form the pyramid
        for (int hash = 0; hash < row; hash++)
        {
            printf("#");  // Print a hash
        }
         // Move to the next line after finishing a row
        printf("\n");
    }

}



