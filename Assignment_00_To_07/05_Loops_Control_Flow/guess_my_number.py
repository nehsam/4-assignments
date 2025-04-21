import random

def main():
    # Function to validate if the input is an integer
    def get_guess():
        while True:
            try:
                return int(input("Enter a guess: "))  # User input as integer
            except ValueError:
                print("Invalid input! Please enter an integer.")
    
    while True:
        # Computer randomly chooses a number from 0 to 99
        secret_number = random.randint(0, 99)
        print("I am thinking of a number between 0 and 99...")

        # Max attempts limit
        attempts = 10
        while attempts > 0:
            guess = get_guess()  # Get valid input
            
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break
            
            attempts -= 1
            print(f"You have {attempts} attempts left.")
        
        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The correct number was: {secret_number}")
        
        # Play again option
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == '__main__':
    main()
