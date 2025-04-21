def display_last_item(items):
    """Displays the last item from a non-empty list."""
    print("The last item in the list is:", items[-1])

def main():
    # List input lene ka tareeqa
    num_items = int(input("How many items will your list contain? "))
    items = []

    for index in range(num_items):
        item = input(f"Enter item {index + 1}: ")
        items.append(item)  # List me item shamil karna

    # Last item ko display karne ke liye function call
    display_last_item(items)

# Program start hone ka entry point
if __name__ == '__main__':
    main()
