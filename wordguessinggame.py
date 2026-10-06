import random

# ---------------- Number Guessing Game ----------------
def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    score = 100  # start with 100 points

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess == number_to_guess:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                print(f"Your score: {score}")
                break
            elif guess < number_to_guess:
                print("Too low! Try again.")
                score -= 5
            else:
                print("Too high! Try again.")
                score -= 5

        except ValueError:
            print("Invalid input. Please enter a number.")

# ---------------- Word Counter ----------------
def word_counter():
    print("\n--- Word Counter ---")
    filename = input("Enter the text file name (e.g., sample.txt): ")

    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            words = text.split()

            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

            print("\nWord Frequency Analysis:")
            for word, count in word_freq.items():
                print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found. Please check the filename.")

# ---------------- Main Menu ----------------
def main():
    while True:
        print("\n=== Number Guessing Game & Word Counter ===")
        print("1. Play Number Guessing Game")
        print("2. Run Word Counter")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            word_counter()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
