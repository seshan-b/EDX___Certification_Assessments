////// Breaking down the problem
// "vote" Function
// Look for a Candidate called name.
// If Candidate found, update their vote total and return true.
// If no candidate found don't update any vote totals and return false

// "print_winner" Function
// Print the name of the candidate(s) who have most votes


#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // Loop through the array of candidates
    // Iterate over each candidate to find a match with the given name
    for (int i = 0; i < candidate_count; i++)
    {
        // Check if the candidate name matches the given name
        // Use strcmp to compare the candidate's name with the provided name
        // strcmp returns 0 if the two strings are identical
        if (strcmp(candidates[i].name, name) == 0)
        {
            // If a match is found, update the vote count
            // Increment the votes count for the matched candidate by 1
            candidates[i].votes++;

            // Return true indicating the vote was successful
            // Since we found the candidate and updated the vote, return true
            return true;
        }
    }

    // If no candidate is found, return false
    // After checking all candidates, if no match is found, return false
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // Initialize max_votes to 0
    // This variable will store the highest number of votes any candidate has received
    int max_votes = 0;

    // Determine the maximum number of votes
    // Loop through all the candidates to find out the highest vote count
    for (int i = 0; i < candidate_count; i++)
    {
        // Check if the current candidate's votes are greater than max_votes
        if (candidates[i].votes > max_votes)
        {
            // Update max_votes to the current candidate's votes
            max_votes = candidates[i].votes;
        }
    }

    // Print the name(s) of candidate(s) with the maximum number of votes
    // Loop through the candidates again to print those who have max_votes
    for (int i = 0; i < candidate_count; i++)
    {
        // Check if the current candidate's votes are equal to max_votes
        if (candidates[i].votes == max_votes)
        {
            // Print the candidate's name
            printf("%s\n", candidates[i].name);
        }
    }
}
