#include <stdio.h>

// Function Declerations
int calculate_checksum(long long card_number);


// Prompt the user for input

int main() {
    long long credit_card_number;

    // Prompt the user for input
    printf("Enter your credit card number: ");
    scanf("%lld", &credit_card_number);

    if (credit_card_number == 0) {
        printf("INVALID CARD\n");
        return 0;
    }

    return 0;
}

// Calculate Checksum Check to see if input is or isn't 0
int calculate_checksum(long long card_number) {
    // Multiply every other digit by 2, starting with secod-to-last digit
    // Add those products' digits together.
    // Add the sum to sum of the digits that wern't multiplied by 2
    // If the total's last digit is 0, number is valid!
    int sum = 0;
    int is_second = 0;
    int digit;

    while (card_number > 0) {
        digit = card_number % 10;
        if (is_second) {
            digit *= 2;
            // Add the digits of the product
            sum += digit / 10;
            sum += digit % 10;
        } else {
            sum += digit;
        }
        card_number /= 10;
        is_second = !is_second;
    }

    return sum;
}
// Check Credit Card length and starting digits.

// Print AMEX, MASTERCARD, VISA or INVALID CARD
