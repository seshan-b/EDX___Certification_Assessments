#include <cs50.h>  // Include the cs50 library to use the get_string function
#include <stdio.h> // Include the standard input-output library for printf
#include <string.h> // Include the string library to use string functions

// Function prototype for comparing scores and printing the winner
void print_winner(int score1, int score2);

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

    // Initialize the score for the first word to 0
    int score1 = 0;
    // Iterate through each character in the first word
    for (int i = 0, n = strlen(word1); i < n; i++)
    {
        // Add the ASCII value of the current character to score1
        score1 += (int) word1[i];
    }
    // Print the score of the first word (for debugging)
    printf("Score of first word: %d\n", score1);

    // Initialize the score for the second word to 0
    int score2 = 0;
    // Iterate through each character in the second word
    for (int i = 0, n = strlen(word2); i < n; i++)
    {
        // Add the ASCII value of the current character to score2
        score2 += (int) word2[i];
    }
    // Print the score of the second word (for debugging)
    printf("Score of second word: %d\n", score2);

    // Call the function to compare scores and print the winner
    print_winner(score1, score2);
}

// Function definition for comparing scores and printing the winner
void print_winner(int score1, int score2)
{
    // Compare the scores of the two words
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
