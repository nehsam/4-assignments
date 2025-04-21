"""
Dice rolling simulation: Randomly rolls two dice and displays their individual results and total.
"""

import random  # Random library import for simulating dice rolls

NUM_SIDES = 6  # Number of sides on each dice

def main():
    print("Rolling two dice... 🎲🎲")
    
    # Randomly roll the dice
    die1 = random.randint(1, NUM_SIDES)  # First dice result
    die2 = random.randint(1, NUM_SIDES)  # Second dice result
    
    # Calculate the total
    total = die1 + die2
    
    # Display the results
    print(f"First dice rolled: {die1}")
    print(f"Second dice rolled: {die2}")
    print(f"Total of both dice: {total} 🎉")


# Required line to run the program
if __name__ == '__main__':
    main()
