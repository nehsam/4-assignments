def double_numbers(numbers):
    """Function to double each number in the list."""
    return [num * 2 for num in numbers]  # Using list comprehension for simplicity

def main():
    # Prompt the user for a list of numbers
    print("Enter numbers separated by spaces to double them:")
    numbers = list(map(int, input().split()))  # Convert input to a list of integers

    # Double the numbers using the custom function
    doubled_list = double_numbers(numbers)

    # Display the results
    print("\nOriginal List:", numbers)
    print("Doubled List:", doubled_list)

if __name__ == '__main__':
    main()
