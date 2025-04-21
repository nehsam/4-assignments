def access_element(my_list, index):
    """Returns the element at the given index or an error message."""
    return f"Element at index {index}: {my_list[index]}" if 0 <= index < len(my_list) else "Index out of range!"

def modify_element(my_list, index, new_value):
    """Modifies the element at the given index or returns an error."""
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"Updated list: {my_list}"
    return "Index out of range!"

def slice_list(my_list, start, end):
    """Returns a sliced list with proper index handling."""
    return f"Sliced list: {my_list[start:end]}" if 0 <= start < len(my_list) and 0 <= end <= len(my_list) else "Invalid indices!"

def main():
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    
    operations = {
        "1": ("Access", access_element),
        "2": ("Modify", modify_element),
        "3": ("Slice", slice_list),
        "4": ("Exit", None)
    }
    
    while True:
        print("\nOperations: 1. Access  2. Modify  3. Slice  4. Exit")
        choice = input("Choose an operation: ")

        if choice in operations:
            if choice == "4":
                print("Goodbye!")
                break
            
            index = int(input("Enter index: "))
            if choice == "2":
                new_value = input("Enter new value: ")
                print(operations[choice][1](my_list, index, new_value))
            else:
                print(operations[choice][1](my_list, index))
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
