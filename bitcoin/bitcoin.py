# ### Breaking down the problem
# Expects the user to specify as a command-line argument the number of Bitcoins, that they would like to buy.
# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
# Returns a JSON object, among whose nested keys is the current price
# Bitcoin as a float Catch any exceptions
# Catch the exceptions in a try statement
# Outputs the current cost of Bitcoins in USD to four decimal places, using as a thousands separator.
# Print format print(f"${amount:,.4f}")


import sys  # Import the sys module

# Get the command-line argument which represents the number of Bitcoins.
if len(sys.argv) != 2:  # Check if the user provided exactly one argument.
    sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")  # Exit with an error message if not.

# Try to convert the command-line argument to a float.
try:
    number_of_bitcoins = float(sys.argv[1])  # Attempt to convert the input to a float.
except ValueError:  # If conversion fails, catch the ValueError exception.
    sys.exit("Error: The input must be a numeric value.")  # Exit with an error message.
