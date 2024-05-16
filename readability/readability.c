#include <ctype.h>    // Include ctype.h for character classification functions
#include <cs50.h>     // Include cs50.h for the get_string function
#include <math.h>     // Include math.h for mathematical functions like round
#include <stdio.h>    // Include stdio.h for input and output functions
#include <string.h>   // Include string.h for string manipulation functions

// The Algo
// index = 0.0588 * L - 0.296 * S - 15.8

// Function prototypes or Function hoisting
int count_letters(string text);      // Declare the function that counts letters
int count_words(string text);        // Declare the function that counts words
int count_sentences(string text);    // Declare the function that counts sentences

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Enter some text: "); // Use get_string to get input from the user and store it in the variable 'text'

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);     // Call count_letters to get the number of letters in 'text'
    int words = count_words(text);         // Call count_words to get the number of words in 'text'
    int sentences = count_sentences(text); // Call count_sentences to get the number of sentences in 'text'

    // Compute the Coleman-Liau index
    float L = (float)letters / words * 100; // Calculate the average number of letters per 100 words
    // S is the average number of sentences per 100 words
    float S = (float)sentences / words * 100; // Calculate the average number of sentences per 100 words
    // Compute the index using the formula
    float index = 0.0588 * L - 0.296 * S - 15.8; // Use the formula to compute the Coleman-Liau index

    // Round the index to the nearest whole number
    int grade = round(index); // Round the index to the nearest integer

    // Print the grade level
    if (grade < 1) // If the grade is less than 1
    {
        printf("Before Grade 1\n"); // Print "Before Grade 1"
    }
    else if (grade >= 16) // If the grade is 16 or higher
    {
        printf("Grade 16+\n"); // Print "Grade 16+"
    }
    else // If the grade is between 1 and 15
    {
        printf("Grade %d\n", grade); // Print the grade level
    }

    // Test Printing
    // printf("Letters: %d\n", letters);   // Print the number of letters
    // printf("Words: %d\n", words);       // Print the number of words
    // printf("Sentences: %d\n", sentences); // Print the number of sentences

    return 0; // Return 0 to indicate successful execution
}

int count_letters(string text)
{
    // Return the number of letters in text
    int count = 0; // Initialize the letter count to 0
    // Iterate through each character in the string
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Check if the character is a letter
        if (isalpha(text[i]))
        {
            count++; // Increment the count if the character is a letter
        }
    }
    return count; // Return the total number of letters
}

int count_words(string text)
{
    // Return the number of words in text
    int count = 1; // Start with 1 assuming there's at least one word
    // Iterate through each character in the string
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Check if the character is a space
        if (text[i] == ' ')
        {
            count++; // Increment the count if the character is a space
        }
    }
    return count; // Return the total number of words
}

int count_sentences(string text)
{
    // Return the number of sentences in text
    int count = 0; // Initialize the sentence count to 0
    // Iterate through each character in the string
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Check if the character is a sentence terminator ('.', '!', or '?')
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++; // Increment the count if the character is a sentence terminator
        }
    }
    return count; // Return the total number of sentences
}
