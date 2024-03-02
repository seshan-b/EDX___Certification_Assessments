

# Create a function for adding subtracting, multiplying and dividing.

def perform_operations(a, b):

    addition_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b

    return addition_result, subtraction_result, multiplication_result, division_result



def main():
    # Take user input for two numbers
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print(perform_operations(a, b))


main()
