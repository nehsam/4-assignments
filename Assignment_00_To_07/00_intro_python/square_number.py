def main():
    print("THIS PROGRAM CALCULATES THE SQUARE OF A NUMBER.")
    # Prompt the user for a number
    square_number = float (input("enter a square number: "))

    
    square = square_number ** 2
    
    # Display the result
    print(f"The square of {square_number} is: {square}")

if __name__ == "__main__":
    main()