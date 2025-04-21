def main():
    from collections import defaultdict  # Dictionary for default count
    
    # Dictionary to store the count of numbers
    num_counts = defaultdict(int)

    print("\033[92mEnter numbers one by one. Press Enter without typing to finish.\033[0m")  # Green text

    while True:
        user_input = input("\033[94mEnter a number (or press Enter to stop): \033[0m")  # Blue text
        
        # Stop input if user presses Enter without typing anything
        if user_input == "":
            break
        
        try:
            # Convert input to an integer
            number = int(user_input)
            # Increase count in dictionary
            num_counts[number] += 1
        except ValueError:
            print("\033[91mInvalid input! Please enter a valid number.\033[0m")  # Red text for errors

    # Print the count of each number
    print("\n\033[93mNumber occurrences:\033[0m")  # Yellow text for header
    for num, count in sorted(num_counts.items()):  # Sort for better readability
        print(f"\033[96m{num}\033[0m appears \033[95m{count}\033[0m times.")  # Cyan and Purple text

# Required line to run the main() function
if __name__ == '__main__':
    main()
