import random

def get_difficulty():
    
    while True:
        print("\nSelect a difficulty level:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-500)")
        
        choice = input("Enter your choice (1,2,3): ")
        if choice == "1":
            return 50
        elif choice == "2":
            return 100
        elif choice == "3":
            return 500
        else:
            print("Invalid choice. Please select Easy, Medium, or Hard.")

def play_game():
    """Main game logic."""
    print("\nWelcome to the Guess the Number Game!")
    max_number = get_difficulty()
    secret_number = random.randint(1, max_number)
    attempts = 0
    score = 100

    print(f"\nI have selected a number between 1 and {max_number}. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if attempts >1:
             score -= 5  # Deduct 5 point per attempt
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                print(f"Your score: {score}")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
def main():
    """Runs the game and handles replay logic."""
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
