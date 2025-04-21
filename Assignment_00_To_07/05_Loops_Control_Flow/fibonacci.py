def main():
    # User se MAX_VALUE input lena
    MAX_VALUE = int(input("Enter the maximum value for Fibonacci sequence: "))

    # Starting values of Fibonacci sequence
    a, b = 0, 1
    
    # List to store Fibonacci numbers (optional)
    fib_numbers = []
    
    # Print Fibonacci numbers until we reach MAX_VALUE
    while a < MAX_VALUE:
        fib_numbers.append(a)  # Store Fibonacci number
        a, b = b, a + b  # Update Fibonacci numbers
    
    # Print Fibonacci numbers space-separated
    print("Fibonacci sequence up to", MAX_VALUE, "is:")
    print(*fib_numbers)
    
    # Print the total count of Fibonacci numbers
    print(f"Total Fibonacci numbers: {len(fib_numbers)}")

# Required to call the main function
if __name__ == '__main__':
    main()
