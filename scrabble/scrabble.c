#include <ctype.h>  // Include the ctype library for handling character type functions like isupper and islower
#include <cs50.h>   // Include the cs50 library to use the get_string function to get user input
#include <stdio.h>  // Include the standard input-output library to use functions like printf to print output
#include <string.h> // Include the string library to use functions like strlen to get the length of a string

// Define an array that assigns points to each letter of the alphabet
// For example, A = 1 point, B = 3 points, C = 3 points, etc.
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Declare a function named compute_score that will calculate the score of a word
int compute_score(string word);

int main(void)
{
    // Prompt the user to enter a word for player 1 and store it in a variable called word1
    string word1 = get_string("Player 1: ");
    // Prompt the user to enter a word for player 2 and store it in a variable called word2
    string word2 = get_string("Player 2: ");

    // Calculate the score of the word entered by player 1 using the compute_score function
    int score1 = compute_score(word1);
    // Calculate the score of the word entered by player 2 using the compute_score function
    int score2 = compute_score(word2);

    // Compare the scores of the two players to determine the winner
    if (score1 > score2)
    {
        // If player 1's score is higher, print "Player 1 wins!"
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        // If player 2's score is higher, print "Player 2 wins!"
        printf("Player 2 wins!\n");
    }
    else
    {
        // If both scores are equal, print "Tie!"
        printf("Tie!\n");
    }
}

// Define the compute_score function that takes a word as input and returns the score of that word
int compute_score(string word)
{
    // Initialize the score to 0
    int score = 0;

    // Loop through each character in the word
    // strlen(word) gets the length of the word, and we loop from 0 to length - 1
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        // Check if the current character is an uppercase letter
        if (isupper(word[i]))
        {
            // If it is uppercase, subtract 'A' from the character to get the index in POINTS array
            // For example, 'A' - 'A' is 0, 'B' - 'A' is 1, etc.
            // Add the points for this letter to the score
            score += POINTS[word[i] - 'A'];
        }
        // Check if the current character is a lowercase letter
        else if (islower(word[i]))
        {
            // If it is lowercase, subtract 'a' from the character to get the index in POINTS array
            // For example, 'a' - 'a' is 0, 'b' - 'a' is 1, etc.
            // Add the points for this letter to the score
            score += POINTS[word[i] - 'a'];
        }
    }

    // Return the total score for the word
    return score;
}
