def subtract_seven(num):
    return num - 7  # Subtracts 7 from the given number

def main():
    number = int(input("Enter a number: "))  # Get user input
    result = subtract_seven(number)  # Call the helper function
    print(f"Result after subtracting 7 from {number}: {result}")  # Print the result with context

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
