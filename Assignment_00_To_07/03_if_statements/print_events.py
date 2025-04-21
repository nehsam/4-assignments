def print_even_numbers(limit):
    """Prints even numbers up to a specified limit."""
    for i in range(limit):
        print(i * 2, end=" ")  # Print even numbers with space separation
    print()  # Print a newline at the end

def main():
    print("Even numbers (up to 20):")
    print_even_numbers(20)  # Call the function to print even numbers


if __name__ == '__main__':
    main()
