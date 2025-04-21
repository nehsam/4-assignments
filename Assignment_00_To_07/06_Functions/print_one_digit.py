def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    try:
        num = int(input("Enter a number: "))  # Try converting input to integer
        print_ones_digit(num)
    except ValueError:
        print("Please enter a valid integer.")  # Handle invalid input

if __name__ == '__main__':
    main()
