#include <cs50.h>
#include <stdio.h>
#include <ctype.h>  // Include ctype.h for isdigit and isalpha functions
#include <stdlib.h> // Include stdlib.h for atoi function
#include <string.h> // Include string.h for strlen function

int main(int argc, string argv[])
{
    // Pseudocode:
    // 1. Make sure program was run with just one command-line argument
    // 2. Make sure every character in argv[1] is a digit
    // 3. Convert argv[1] from a `string` to an `int`
    // 4. Prompt user for plaintext
    // 5. For each character in the plaintext:
    //    a. Rotate the character if it's a letter

    // Make sure program was run with just one command-line argument
    if (argc != 2)
    {
        // Print usage message if the number of command-line arguments is not 2
        printf("Usage: ./caesar key\n");
        return 1; // Return an error code
    }

    // Make sure every character in argv[1] is a digit
    for (int i = 0; argv[1][i] != '\0'; i++)
    {
        // Check if the current character is not a digit
        if (!isdigit(argv[1][i]))
        {
            // Print usage message if any character is not a digit
            printf("Usage: ./caesar key\n");
            return 1; // Return an error code
        }
    }

    // Convert argv[1] from a `string` to an `int`
    int key = atoi(argv[1]); // Convert the key from a string to an integer

    // Prompt user for plaintext
    string plaintext = get_string("plaintext: "); // Get the plaintext input from the user

    // For each character in the plaintext:
    printf("ciphertext: "); // Print the label for the ciphertext
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        // Check if the current character is a letter
        if (isalpha(plaintext[i]))
        {
            // Rotate the character if it's a letter
            // Determine the ASCII offset based on whether the letter is uppercase or lowercase
            char offset = isupper(plaintext[i]) ? 'A' : 'a';
            // Rotate the letter and print the resulting character
            printf("%c", (plaintext[i] - offset + key) % 26 + offset);
        }
        else
        {
            // Print the character as it is if it's not a letter
            printf("%c", plaintext[i]);
        }
    }
    printf("\n"); // Print a newline after the ciphertext

    return 0; // Return 0 to indicate successful completion
}
