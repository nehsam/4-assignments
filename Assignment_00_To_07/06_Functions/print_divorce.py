import math

def print_divisors(num):
    # Loop only up to the square root of the number to find divisors
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(i, end=' ')  # Print the divisor
            if i != num // i:  # To avoid printing the square root twice
                print(num // i, end=' ')  # Print the corresponding pair divisor
    print()  # Print a newline after all divisors

def main():
    # Get user input
    num = int(input("Enter a number: "))
    print(f"Here are the divisors of {num}")
    print_divisors(num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
