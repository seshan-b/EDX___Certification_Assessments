////// Breaking down the problem

// vote function
// The function takes arguments rank, name, and ranks. If name is a match for the name of a valid candidate, then you should update the ranks array to indicate that the voter has the candidate as their rank preference (where 0 is the first preference, 1 is the second preference, etc.)
// Recall that ranks[i] here represents the user’s ith preference.
// The function should return true if the rank was successfully recorded, and false otherwise (if, for instance, name is not the name of one of the candidates).
// You may assume that no two candidates will have the same name.

// "record_preferences" function
// The function is called once for each voter, and takes as argument the ranks array, (recall that ranks[i] is the voter’s ith preference, where ranks[0] is the first preference).
// The function should update the global preferences array to add the current voter’s preferences. Recall that preferences[i][j] should represent the number of voters who prefer candidate i over candidate j.
// You may assume that every voter will rank each of the candidates.

// add_pairs function
// The function should add all pairs of candidates where one candidate is preferred to the pairs array. A pair of candidates who are tied (one is not preferred over the other) should not be added to the array.
// The function should update the global variable pair_count to be the number of pairs of candidates. (The pairs should thus all be stored between pairs[0] and pairs[pair_count - 1], inclusive).

// sort_pairs function
// The function should sort the pairs array in decreasing order of strength of victory, where strength of victory is defined to be the number of voters who prefer the preferred candidate. If multiple pairs have the same strength of victory, you may assume that the order does not matter.

// lock_pairs function
// The function should create the locked graph, adding all edges in decreasing order of victory strength so long as the edge would not create a cycle.

// print_winner function
// The function should print out the name of the candidate who is the source of the graph. You may assume there will not be more than one source.


#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is the number of voters who prefer candidate i over candidate j
int preferences[MAX][MAX];

// locked[i][j] means candidate i is locked in over candidate j
bool locked[MAX][MAX];

// Each pair has a winner and a loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidate names
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2]; // Array to store pairs of candidates

int pair_count; // Number of pairs
int candidate_count; // Number of candidates

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool creates_cycle(int winner, int loser);
int strength_of_victory(pair p);

int main(int argc, string argv[])
{
    // Check if there are enough arguments (candidates)
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate the array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Initialize the locked matrix to false
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        int ranks[candidate_count]; // ranks[i] is voter's ith preference

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// vote function updates ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// record_preferences function updates preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
}

// add_pairs function records pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    pair_count = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (i != j && preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
        }
    }
}

// strength_of_victory function calculates the strength of victory for a pair
int strength_of_victory(pair p)
{
    return preferences[p.winner][p.loser] - preferences[p.loser][p.winner];
}

// sort_pairs function sorts pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    for (int i = 0; i < pair_count - 1; i++)
    {
        for (int j = 0; j < pair_count - i - 1; j++)
        {
            if (strength_of_victory(pairs[j]) < strength_of_victory(pairs[j + 1]))
            {
                pair temp = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = temp;
            }
        }
    }
}

// lock_pairs function locks pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        if (!creates_cycle(pairs[i].winner, pairs[i].loser))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
}

// creates_cycle function checks if locking a pair creates a cycle
bool creates_cycle(int winner, int loser)
{
    if (loser == winner)
    {
        return true;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[loser][i])
        {
            if (creates_cycle(winner, i))
            {
                return true;
            }
        }
    }
    return false;
}

// print_winner function prints the winner of the election
void print_winner(void)
{
    // Iterate over each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        bool is_source = true; // Assume candidate i is a source

        // Check if candidate i is locked by any other candidate
        for (int j = 0; j < candidate_count; j++)
        {
            // If candidate j has an edge locked over candidate i
            if (locked[j][i])
            {
                is_source = false; // Candidate i is not a source
                break; // No need to check further, break out of the loop
            }
        }

        // If candidate i is a source (no one has locked an edge over them)
        if (is_source)
        {
            printf("%s\n", candidates[i]); // Print the name of the candidate
            break; // We found the source, no need to check further, break out of the loop
        }
    }
}
