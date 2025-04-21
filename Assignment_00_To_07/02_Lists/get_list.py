def main():
    print("Start entering values for your list. Press Enter without typing anything to stop.")
    values_list = []  # List to store user inputs

    while True:
        value = input("Enter a value: ")  # Taking input from the user
        
        if value.strip() == "":  # Check for empty input (ignoring spaces)
            break  # Exit the loop when user presses Enter
        
        values_list.append(value)  # Add non-empty value to the list

    if values_list:
        print("\nYou created the following list:")
        print(values_list)
    else:
        print("\nNo values were added to the list.")

# Entry point for the program
if __name__ == '__main__':
    main()
