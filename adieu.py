import inflect

def main():
    # Create an instance of inflect engine
    p = inflect.engine()

    # Initialize an empty list to store names
    names = []

    print("Enter names one per line (press Control-D to end):")

    # Collect names until EOF (Control-D)
    try:
        while True:
            name = input()
            if name:
                names.append(name)
    except EOFError:
        pass  # Exit loop on Control-D

    # Join names with correct grammar using inflect
    farewell_message = f"Adieu, adieu, to {p.join(names)}"

    # Print the farewell message
    print(farewell_message)

# Run the main function
if __name__ == "__main__":
    main()
