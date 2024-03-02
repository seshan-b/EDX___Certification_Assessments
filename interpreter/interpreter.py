

# Create a function for adding subtracting, multiplying and dividing.

def perform_operations(user_input):


    # Split the expression into numbers and operation
    x, operation, y = user_input.split()

    # Convert numbers to float
    num1 = float(num1)
    num2 = float(num2)

    match operation:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/' if y != 0:
            return x / y



def main():
     user_input = input("Enter an expression (1 + 1): ")
     return user_input


main()
