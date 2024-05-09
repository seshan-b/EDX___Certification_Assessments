#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed (in cents): ");
    }
    while (cents < 0);

    // Calculate how many quarters you should give customer
    int quarters = cents / 25;
    // Subtract the value of those quarters from cents
    cents = cents % 25;


    // Calculate how many dimes you should give customer
    int dimes = cents / 10;
    // Subtract the value of those dimes from remaining cents
    cents = cents % 10;


    // Calculate how many nickels you should give customer
    // Subtract the value of those nickels from remaining cents

    // Calculate how many pennies you should give customer
    // Subtract the value of those pennies from remaining cents

    // Sum the number of quarters, dimes, nickels, and pennies used
    // Print that sum
}
