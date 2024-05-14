#include <stdio.h>

// Sudo Code



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
    int sum = 0;
    int digit;
    int is_second = 0;

    while (card_number > 0) {
        digit = card_number % 10;
        if (is_second) {
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }
        sum += digit;
        card_number /= 10;
        is_second = !is_second;
    }

    return sum;
}

// Check Credit Card length and starting digits.

// Print AMEX, MASTERCARD, VISA or INVALID CARD
