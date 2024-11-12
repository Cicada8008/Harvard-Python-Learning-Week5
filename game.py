import random

def get_positive_integer(prompt):
    while True:
        try:
            # Attempt to convert input to an integer
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

def main():
    # Prompt for level
    level = get_positive_integer("Level: ")

    # Generate a random number between 1 and the given level
    target = random.randint(1, level)

    # Guessing loop
    while True:
        guess = get_positive_integer("Guess: ")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

# Run the main function
if __name__ == "__main__":
    main()
