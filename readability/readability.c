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
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Count the number of letters, words, and sentences in the text

    // Compute the Coleman-Liau index

    // Print the grade level


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
