#include <ctype.h>  // Include the ctype library for character type functions like isupper and islower
#include <cs50.h>   // Include the cs50 library for the get_string function
#include <stdio.h>  // Include the standard input-output library for printf
#include <string.h> // Include the string library for functions like strlen

// Points assigned to each letter of the alphabet
// A = 1, B = 3, C = 3, D = 2, E = 1, F = 4, G = 2, H = 4, I = 1, J = 8, K = 5, L = 1, M = 3, N = 1, O = 1, P = 3, Q = 10, R = 1, S = 1, T = 1, U = 1, V = 4, W = 4, X = 8, Y = 4, Z = 10
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Function prototype for computing the score of a word
int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    // Get the first word from player 1
    string word1 = get_string("Player 1: ");
    // Get the second word from player 2
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    // Compute the score of the first word
    int score1 = compute_score(word1);
    // Compute the score of the second word
    int score2 = compute_score(word2);

    // Print the winner
    // Compare the scores and determine the winner
    if (score1 > score2)
    {
        // If player 1's score is higher, print that player 1 wins
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        // If player 2's score is higher, print that player 2 wins
        printf("Player 2 wins!\n");
    }
    else
    {
        // If scores are equal, print that it's a tie
        printf("Tie!\n");
    }
}

// Function definition for computing the score of a word
int compute_score(string word)
{
    // Keep track of score
    // Initialize the score to 0
    int score = 0;

    // Compute score for each character
    // Iterate through each character in the word
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        // If the character is uppercase
        if (isupper(word[i]))
        {
            // Subtract 'A' to get the index and add the corresponding points
            score += POINTS[word[i] - 'A'];
        }
        // If the character is lowercase
        else if (islower(word[i]))
        {
            // Subtract 'a' to get the index and add the corresponding points
            score += POINTS[word[i] - 'a'];
        }
    }

    // Return the computed score
    return score;
}
