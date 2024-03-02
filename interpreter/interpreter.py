

# Create a function for adding subtracting, multiplying and dividing.
def perform_operations(user_input):

    # Split the expression into numbers and operation
    # Default splits by space
    x, operation, y = user_input.split()

    # Convert numbers to float
    x = float(x)
    y = float(y)

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
    while True:
        user_input = input("Enter an expression (1 + 1): ")
        print(perform_operations(user_input))
        return perform_operations(user_input)

main()
