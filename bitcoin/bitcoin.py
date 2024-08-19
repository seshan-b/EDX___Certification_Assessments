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
import requests  # Import the requests module to make the HTTP request.


# Get the command-line argument which represents the number of Bitcoins.
if len(sys.argv) != 2:  # Check if the user provided exactly one argument.
    sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")  # Exit with an error message if not.

# Try to convert the command-line argument to a float.
try:
    number_of_bitcoins = float(sys.argv[1])  # Attempt to convert the input to a float.
except ValueError:  # If conversion fails, catch the ValueError exception.
    sys.exit("Error: The input must be a numeric value.")  # Exit with an error message.


# Make a GET request to the CoinDesk API.
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")  # Perform the GET request.
    response.raise_for_status()  # Check if the request was successful (status code 200).
except requests.RequestException as e:  # Catch any request-related exceptions.
    sys.exit(f"Error: Failed to fetch data from CoinDesk API. {e}")  # Exit with an error message.

# Parse the JSON response to extract the current Bitcoin price.
try:
    data = response.json()  # Parse the JSON data from the response.
    # Navigate through the nested JSON to get the current price in USD.
    current_price = float(data["bpi"]["USD"]["rate_float"])
except (KeyError, TypeError, ValueError) as e:  # Catch exceptions related to JSON parsing or missing data.
    sys.exit(f"Error: Failed to parse the Bitcoin price from the response. {e}")  # Exit with an error message.


# Perform the calculation to determine the total cost.
try:
    total_cost = number_of_bitcoins * current_price  # Calculate the total cost.
except Exception as e:  # Catch any general exceptions that might occur during the calculation.
    sys.exit(f"Error: An unexpected error occurred during the calculation. {e}")  # Exit with an error message.

# Format the result to four decimal places with a thousands separator.
try:
    formatted_cost = f"${total_cost:,.4f}"  # Format the total cost to four decimal places and add thousands separators.
except Exception as e:  # Catch any exceptions related to string formatting.
    sys.exit(f"Error: An unexpected error occurred while formatting the output. {e}")  # Exit with an error message.

# Output the formatted result to the user.
print(formatted_cost)  # Display the formatted total cost.
