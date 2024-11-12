import sys
import requests

def main():
    # Check for exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    # Try to convert the argument to a float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Please provide a valid number of bitcoins.")

    # Fetch the current Bitcoin price in USD from the CoinDesk API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Could not retrieve Bitcoin price.")
    except (KeyError, ValueError):
        sys.exit("Error: Unexpected data format from API.")

    # Calculate the total cost
    total_cost = bitcoins * price_per_bitcoin

    # Print the total cost formatted with commas and four decimal places
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
