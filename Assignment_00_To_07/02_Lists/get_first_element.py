def display_first_item(items):
    """Displays the first item from a non-empty list."""
    print("First item in the list:", items[0])

def main():
    # Input for number of elements
    count = int(input("How many items do you want to add to the list? "))
    items = []

    # Taking input for list elements
    for index in range(count):
        value = input(f"Enter item {index + 1}: ")
        items.append(value)

    # Display the first item
    display_first_item(items)

# Standard entry point for the program
if __name__ == '__main__':
    main()
