# ### Breaking down the problem
# Expects the user to specify as a command-line argument the number of Bitcoins, that they would like to buy.
# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
# Returns a JSON object, among whose nested keys is the current price
# Bitcoin as a float Be sure to catch any exceptions
