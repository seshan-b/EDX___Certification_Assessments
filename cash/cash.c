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
     int nickels = cents / 5;
    // Subtract the value of those nickels from remaining cents
    cents = cents % 10;

    // Calculate how many pennies you should give customer
    int pennies = cents;
    // Subtract the value of those pennies from remaining cents

    // Sum the number of quarters, dimes, nickels, and pennies used
    int total_coins = quarters + dimes + nickels + pennies;
    // Print that sum


    // Test Printing
    printf("Quarters: %d\n", quarters);
    printf("Dimes: %d\n", dimes);
    printf("Nickels: %d\n", nickels);
    printf("Remaining cents after quarters, dimes, and nickels: %d\n", cents);
    printf("Total coins used: %d\n", total_coins);
}
