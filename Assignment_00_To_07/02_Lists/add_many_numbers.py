def calculate_sum(numbers):
    """Function to calculate the sum of a list of numbers."""
    return sum(numbers)  # Using Python's built-in sum function for simplicity

def main():
    # Prompt the user for a custom list of numbers
    print("Enter numbers separated by spaces to calculate their sum:")
    numbers_list = list(map(int, input().split()))  # Convert input string to a list of integers

    # Calculate the sum using the custom function
    result = calculate_sum(numbers_list)

    # Display the results
    print("\nYou entered:", numbers_list)
    print("The sum of the numbers is:", result)

if __name__ == '__main__':
    main()
