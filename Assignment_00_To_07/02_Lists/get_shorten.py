MAX_LENGTH = 3  # Define the maximum allowed length

def shorten(lst):
    """Reduces the list size to MAX_LENGTH by removing items from the end."""
    while len(lst) > MAX_LENGTH:  # Check if the list is longer than MAX_LENGTH
        removed_item = lst.pop()  # Remove the last item
        print(f"Removed: {removed_item}")  # Inform the user about the removed item

def main():
    print(f"Create a list, but it will be shortened to a maximum of {MAX_LENGTH} items.")
    user_list = []  # Initialize an empty list

    # Get user input for the list
    n = int(input("How many elements would you like to add? "))
    for i in range(n):
        value = input(f"Enter value {i + 1}: ")
        user_list.append(value)  # Add the value to the list

    print("\nOriginal list:", user_list)  # Show the original list
    if len(user_list) > MAX_LENGTH:
        print("\nShortening the list...")
        shorten(user_list)  # Call the shorten function
    else:
        print("\nNo shortening needed. The list is within the allowed length.")

    print("Final list:", user_list)  # Show the final shortened list


if __name__ == '__main__':
    main()
