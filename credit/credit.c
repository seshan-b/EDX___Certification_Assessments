#include <stdio.h>  // Includes the standard input/output library

// Function to calculate the checksum of the credit card number
int calculate_checksum(long long card_number) {
        int sum = 0;  // Variable to store the sum of digits
        int is_second = 0;  // Flag to indicate every other digit
        int digit;  // Variable to store the current digit

        // Loop through each digit of the card number
        while (card_number > 0) {
            digit = card_number % 10;  // Extract the last digit

            if (is_second)
            {
                digit *= 2;  // Double every other digit
                // Add the digits of the product
                sum += digit / 10;  // Add the tens place digit
                sum += digit % 10;  // Add the units place digit
            }
            else
            {
                sum += digit;  // Add the digit directly if not doubled
            }

            card_number /= 10;  // Remove the last digit
            is_second = !is_second;  // Toggle the flag for every other digit
        }

        return sum;  // Return the calculated sum
}

// Function to get the length of the credit card number
int get_card_length(long long card_number) {

        int length = 0;  // Variable to store the length of the card number

        // Loop through each digit of the card number
        while (card_number > 0)
        {
            card_number /= 10;  // Remove the last digit
            length++;  // Increment the length counter
        }

        return length;  // Return the length of the card number
}

// Function to get the starting digits of the credit card number
int get_starting_digits(long long card_number, int num_digits) {

        long long divisor = 1;  // Variable to calculate the divisor for extracting starting digits

        // Loop to set the divisor
        for (int i = 0; i < get_card_length(card_number) - num_digits; i++)
        {
            divisor *= 10;  // Increase the divisor to move left the required number of digits
        }

        return card_number / divisor;  // Extract the starting digits
}

// Function to check the type of credit card based on length and starting digits
void check_card_type(long long card_number) {

        int length = get_card_length(card_number);  // Get the length of the card number
        int starting_digits = get_starting_digits(card_number, 2);  // Get the first two digits of the card number

        // Check the card type based on length and starting digits
        if (length == 15 && (starting_digits == 34 || starting_digits == 37))
        {
            printf("AMEX\n");  // American Express
        }
        else if (length == 16 && (starting_digits >= 51 && starting_digits <= 55))
        {
            printf("MASTERCARD\n");  // MasterCard
        }
        else if ((length == 13 || length == 16) && (starting_digits / 10 == 4))
        {
            printf("VISA\n");  // Visa
        }
        else
        {
            printf("INVALID\n");  // Invalid card
        }
}

int main() {
        long long credit_card_number;  // Variable to store the credit card number

        // Prompt the user for input
        printf("Enter your credit card number: ");
        scanf("%lld", &credit_card_number);  // Read the input and store it in credit_card_number

        // Check to see if input is or isn't 0
        if (credit_card_number == 0)
        {
            printf("INVALID\n");  // Print "INVALID" if the input is 0
            return 0;  // Exit the program
        }

        // Calculate checksum
        int checksum = calculate_checksum(credit_card_number);  // Call the function to calculate checksum
        if (checksum % 10 != 0)
        {
            printf("INVALID\n");  // Print "INVALID" if the checksum is not divisible by 10
            return 0;  // Exit the program
        }

        // Check credit card length and starting digits
        check_card_type(credit_card_number);  // Call the function to check the card type

        return 0;  // Return 0
}
