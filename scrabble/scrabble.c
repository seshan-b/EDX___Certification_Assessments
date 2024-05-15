#include <cs50.h>  // Include the cs50 library to use the get_string function
#include <stdio.h> // Include the standard input-output library for printf
#include <string.h> // Include the string library to use string functions
#include <ctype.h> // Include the ctype library to use the toupper function

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Function prototype for computing the score of a word
int compute_score(string word);

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

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the score of each word (for debugging)
    printf("Score of first word: %d\n", score1);
    printf("Score of second word: %d\n", score2);

    // Print the winner
    if (score1 > score2)
    {
        // If the score of the first word is greater, print that the first word is the winner
        printf("The first word wins!\n");
    }
    else if (score1 < score2)
    {
        // If the score of the second word is greater, print that the second word is the winner
        printf("The second word wins!\n");
    }
    else
    {
        // If the scores are equal, print that it's a tie
        printf("It's a tie!\n");
    }
}

// Function definition for computing the score of a word
int compute_score(string word)
{
    // Initialize the score to 0
    int score = 0;
    // Iterate through each character in the word
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        // Check if the character is a letter
        if (isalpha(word[i]))
        {
            // Convert the character to uppercase
            char upper_char = toupper(word[i]);
            // Calculate the index by subtracting 'A' from the uppercase character
            int index = upper_char - 'A';
            // Add the points for the character to the score
            score += POINTS[index];
        }
    }
    // Return the computed score
    return score;
}
