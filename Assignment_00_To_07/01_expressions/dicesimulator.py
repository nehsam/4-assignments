import random

NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)

    die2 = random.randint(1, NUM_SIDES)

    total=die1 + die2

    print("Total of two dice:", total)

def main():

    die1 = 10

    print("die1 in main() starts as: " + str(die1))
    
    # Ab hum die ko roll karenge teen baar
    roll_dice()  # Pehla roll
    roll_dice()  # Doosra roll

    # Die1 ka value final print karte hain
    print("die1 in main() is: " + str(die1))

# Ye line zaroori hai taake main function call ho sake
if __name__ == '__main__':
    main()   

    

