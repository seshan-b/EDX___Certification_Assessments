#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// The Algo
// index = 0.0588 * L - 0.296 * S - 15.8


// Function prototypes or Function hoisting
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{

    // Prompt the user for some text
    string text = get_string("Enter some text: ");


    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index
    float L = (float)letters / words * 100;
    // S is the average number of sentences per 100 words
    float S = (float)sentences / words * 100;
    // Compute the index using the formula
    float index = 0.0588 * L - 0.296 * S - 15.8;

     // Round the index to the nearest whole number
    int grade = round(index);

    // Print the grade level
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", grade);
    }


    // Test Printing
    printf("Letters: %d\n", letters);
    printf("Words: %d\n", words);
    printf("Sentences: %d\n", sentences);

}

int count_letters(string text)
{
    // Return the number of letters in text
    int count = 0;
    // Iterate through each character in the string
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Check if the character is a letter
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int count_words(string text)
{
    // Return the number of letters in text
    int count = 1; // Start with 1 assuming there's at least one word
    // Iterate through each character in the string
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Check if the character is a space
        if (text[i] == ' ')
        {
            count++;
        }
    }
    return count;
}


int count_sentences(string text)
{
    // Return the number of letters in text
    int count = 0;
    // Iterate through each character in the string
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Check if the character is a sentence terminator
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}
