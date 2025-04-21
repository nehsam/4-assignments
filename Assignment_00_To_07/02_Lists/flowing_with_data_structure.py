def insert_multiple(my_list, element):
    """Inserts the given element into the list three times."""
    for _ in range(3):  # Repeat the process three times
        my_list.append(element)

def main():
    # Get input from the user
    text = input("What message would you like to repeat? ")

    # Initialize an empty list
    result_list = []
    print("Initial List:", result_list)

    # Call the function to add the element
    insert_multiple(result_list, text)

    # Display the updated list
    print("Updated List:", result_list)

# Standard entry point for the program
if __name__ == '__main__':
    main()
