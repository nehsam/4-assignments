def find_average(numbers):
    return sum(numbers) / len(numbers)  # Sum of numbers divided by total count

def main():
    # Taking input from the user for multiple numbers
    num_list = []
    while True:
        num = input("Enter a number (or press Enter to finish): ")
        if num == "":
            break  # Exit loop if user presses Enter without entering a number
        else:
            num_list.append(float(num))  # Add the number to the list

    # If there are numbers in the list, calculate and display the average
    if num_list:
        average = find_average(num_list)
        print(f"The average of the numbers is: {average}")
    else:
        print("No numbers were entered.")

if __name__ == '__main__':
    main()
