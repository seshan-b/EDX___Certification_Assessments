# ### Breaking down the problem
# Expects the user to specify as a command-line argument the number of Bitcoins, that they would like to buy.
# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
# Returns a JSON object, among whose nested keys is the current price
# Bitcoin as a float Catch any exceptions
# Catch the exceptions in a try statement
# Outputs the current cost of Bitcoins in USD to four decimal places, using as a thousands separator.
# Print format print(f"${amount:,.4f}")


import sys  # For handling command-line arguments and exiting the program.
import requests  # For making the HTTP request to the API.

# Ensure exactly one command-line argument is provided.
if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

# Try to convert the argument to a float, exit with an error if it fails.
try:
    number_of_bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Error: The input must be a numeric value.")

# Request the current Bitcoin price from the CoinDesk API.
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
except requests.RequestException as e:
    sys.exit(f"Error: Failed to fetch data from CoinDesk API. {e}")

# Extract the current price from the JSON response.
try:
    data = response.json()
    current_price = float(data["bpi"]["USD"]["rate_float"])
except (KeyError, TypeError, ValueError) as e:
    sys.exit(f"Error: Failed to parse the Bitcoin price from the response. {e}")

# Calculate the total cost.
try:
    total_cost = number_of_bitcoins * current_price
except Exception as e:
    sys.exit(f"Error: An unexpected error occurred during the calculation. {e}")

# Format the cost to four decimal places with a thousands separator.
try:
    formatted_cost = f"${total_cost:,.4f}"
except Exception as e:
    sys.exit(f"Error: An unexpected error occurred while formatting the output. {e}")

# Print the formatted total cost.
print(formatted_cost)
