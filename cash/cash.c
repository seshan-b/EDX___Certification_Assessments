#include <cs50.h>
#include <stdio.h>


// Function to calculate how many nickels to give the customer
int calculate_nickels(int *remaining_cents)
{
    int nickels = *remaining_cents / 5;
    *remaining_cents = *remaining_cents % 5; // Update remaining cents after using nickels
    return nickels;
}


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


    // Calculate how many nickels you should give the customer using the new function
    int nickels = calculate_nickels(&cents);

    // Calculate how many pennies you should give customer
    int pennies = cents;
    // Subtract the value of those pennies from remaining cents
    // cents = 0;

    // Sum the number of quarters, dimes, nickels, and pennies used
    int total_coins = quarters + dimes + nickels + pennies;



    // Test Printing
    printf("Quarters: %d\n", quarters);
    printf("Dimes: %d\n", dimes);
    printf("Nickels: %d\n", nickels);
    printf("Remaining cents after quarters, dimes, and nickels: %d\n", cents);
    printf("Total coins used: %d\n", total_coins);
}
