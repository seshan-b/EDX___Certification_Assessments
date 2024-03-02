

# Create a function for adding subtracting, multiplying and dividing.

def perform_operations(user_input):


    # Split the expression into numbers and operation
    x, operation, y = user_input.split()

    match operation:
        case 'add':
            return x + y
        case 'subtract':
            return x - y
        case 'multiply':
            return x * y
        case 'divide' if y != 0:
            return x / y



def main():


main()
