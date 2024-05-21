// Include necessary libraries
#include <cs50.h>   // Library for CS50-specific functions, like get_string
#include <stdio.h>  // Standard Input Output library for functions like printf
#include <string.h> // Library for string handling functions, like strlen
#include <ctype.h>  // Library for character handling functions, like isalpha and tolower
#include <stdlib.h> // Standard library for functions like malloc and exit

// Function to check if the program has the correct number of command-line arguments
bool is_valid_arg_count(int argc)
{
    // Check if exactly one command-line argument is provided (the key)
    if (argc != 2)
    {
        // Print error message if the number of arguments is incorrect
        printf("Usage: ./substitution key\n");
        return false;
    }
    return true;
}

// Function to check if the key is valid
bool is_valid_key(string key)
{
    // Check if the key has 26 characters
    if (strlen(key) != 26)
    {
        // Print error message if the key does not have 26 characters
        printf("Key must contain 26 characters.\n");
        return false;
    }

    // Array to keep track of which letters have been seen
    bool seen[26] = {false};

    for (int i = 0; i < 26; i++)
    {
        char c = key[i];
        // Check if the character is alphabetic
        if (!isalpha(c))
        {
            // Print error message if the key contains non-alphabetic characters
            printf("Key must only contain alphabetic characters.\n");
            return false;
        }

        // Convert to lowercase for case-insensitive comparison
        c = tolower(c);

        // Check if the character has already been seen
        if (seen[c - 'a'])
        {
            // Print error message if the key contains repeated characters
            printf("Key must not contain repeated characters.\n");
            return false;
        }

        // Mark this character as seen
        seen[c - 'a'] = true;
    }

    return true;
}

// Function to encrypt the plaintext using the key
char* encrypt(string plaintext, string key)
{
    int n = strlen(plaintext);
    char *ciphertext = malloc(n + 1); // Allocate memory for the ciphertext

    if (ciphertext == NULL) // Check if memory allocation was successful
    {
        printf("Memory allocation failed\n");
        exit(1);
    }

    for (int i = 0; i < n; i++)
    {
        char c = plaintext[i];
        if (isalpha(c))
        {
            // Preserve case
            if (isupper(c))
            {
                ciphertext[i] = toupper(key[c - 'A']);
            }
            else
            {
                ciphertext[i] = tolower(key[c - 'a']);
            }
        }
        else
        {
            ciphertext[i] = c;
        }
    }
    ciphertext[n] = '\0'; // Null-terminate the string

    return ciphertext;
}

// Main Function
int main(int argc, string argv[])
{
    // Pseudocode:
    // 1. Make sure program accepts a single command-line argument, the key to use for the substitution.
    // 2. Make sure the key itself should be case-insensitive, so whether any character in the key is uppercase or
    //    lowercase should not affect the behavior of your program.
    // 3. If your program is executed without any command-line arguments or with more than one command-line argument,
    //    your program should print an error message of your choice (with printf) and return from main a value of 1
    //    (which tends to signify an error) immediately.
    // 4. If the key is invalid (as by not containing 26 characters, containing any character that is not an alphabetic character,
    //    or not containing each letter exactly once), your program should print an error message of your choice (with printf) and return
    //    from main a value of 1 immediately.
    // 5. Must output plaintext: (without a newline) and then prompt the user for a string of plaintext (using get_string).
    // 6. Must output ciphertext: (without a newline) followed by the plaintext’s corresponding ciphertext, with each alphabetical
    //    character in the plaintext substituted for the corresponding character in the ciphertext; non-alphabetical characters should be outputted unchanged.
    // 7. Must preserve case: capitalized letters must remain capitalized letters; lowercase letters must remain lowercase letters.
    // 8. After outputting ciphertext, you should print a newline. Your program should then exit by returning 0 from main.

    // Check if the number of command-line arguments is valid
    if (!is_valid_arg_count(argc))
    {
        // Return 1 to indicate an error if the argument count is invalid
        return 1;
    }

    // Validate the key
    if (!is_valid_key(argv[1]))
    {
        // Return 1 to indicate an error if the key is invalid
        return 1;
    }

    // Output "plaintext: " without a newline
    printf("plaintext: ");

    // Prompt the user for a string of plaintext
    string plaintext = get_string("");

    // Encrypt the plaintext using the key
    char* ciphertext = encrypt(plaintext, argv[1]);

    // Output "ciphertext: " without a newline
    printf("ciphertext: ");

    // Print the ciphertext followed by a newline
    printf("%s\n", ciphertext);

    // Free the allocated memory for ciphertext
    free(ciphertext);

    // Return 0 to indicate successful execution
    return 0;
}
