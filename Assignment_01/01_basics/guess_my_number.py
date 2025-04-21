import random  # Random number generate karne ke liye

def main():
    while True:
        # 0 se 99 ke beech ek random number choose karna
        secret_number = random.randint(0, 99)
        print("I am thinking of a number between 0 and 99...")
        
        attempts = 0  # Attempts counter initialize karna
        
        while True:
            try:
                # User se number input lena
                guess = int(input("Enter a guess: "))
                
                # Input validation
                if guess < 0 or guess > 99:
                    print("Please enter a number between 0 and 99.")
                    continue
                
                attempts += 1  # Attempt increment karna

                # Conditions check karna
                if guess > secret_number:
                    print("Your guess is too high")
                elif guess < secret_number:
                    print("Your guess is too low")
                else:
                    print(f"Congrats! The number was: {secret_number}")
                    print(f"You guessed it in {attempts} attempts.")
                    break  # Correct answer milne par loop end kar dena
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        
        # Replay option
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Main function ko call karna
if __name__ == '__main__':
    main()
