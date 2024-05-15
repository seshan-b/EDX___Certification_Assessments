#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt the user for two words
    // Use get_string from the cs50 library to get the first word from the user
    string word1 = get_string("Enter the first word: ");
    // Print the first word to check if it was correctly inputted (for debugging)
    printf("First word: %s\n", word1);

    // Use get_string from the cs50 library to get the second word from the user
    string word2 = get_string("Enter the second word: ");
    // Print the second word to check if it was correctly inputted (for debugging)
    printf("Second word: %s\n", word2);

}
