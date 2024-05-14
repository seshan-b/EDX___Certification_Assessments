#include <stdio.h>

int calculate_checksum(long long card_number);
int get_card_length(long long card_number);
int get_starting_digits(long long card_number, int num_digits);
void check_card_type(long long card_number);

int main() {
    long long credit_card_number;

    // Prompt the user for input
    printf("Enter your credit card number: ");
    scanf("%lld", &credit_card_number);

    // Check to see if input is or isn't 0
    if (credit_card_number == 0) {
        printf("INVALID CARD\n");
        return 0;
    }

    // Calculate checksum
    int checksum = calculate_checksum(credit_card_number);
    if (checksum % 10 != 0) {
        printf("INVALID CARD\n");
        return 0;
    }

    // Check credit card length and starting digits
    check_card_type(credit_card_number);

    return 0;
}

int calculate_checksum(long long card_number) {
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

int get_card_length(long long card_number) {
    int length = 0;
    while (card_number > 0) {
        card_number /= 10;
        length++;
    }
    return length;
}

int get_starting_digits(long long card_number, int num_digits) {
    long long divisor = 1;
    for (int i = 0; i < get_card_length(card_number) - num_digits; i++) {
        divisor *= 10;
    }
    return card_number / divisor;
}

void check_card_type(long long card_number) {
    int length = get_card_length(card_number);
    int starting_digits = get_starting_digits(card_number, 2);

    printf("Card length: %d\n", length);
    printf("Starting digits: %d\n", starting_digits);

    if (length == 15 && (starting_digits == 34 || starting_digits == 37)) {
        printf("AMEX\n");
    } else if (length == 16 && (starting_digits >= 51 && starting_digits <= 55)) {
        printf("MASTERCARD\n");
    } else if ((length == 13 || length == 16) && (starting_digits / 10 == 4)) {
        printf("VISA\n");
    } else {
        printf("INVALID CARD\n");
    }
}
