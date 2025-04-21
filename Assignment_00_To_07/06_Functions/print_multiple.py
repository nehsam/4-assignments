def print_multiple(message: str, repeats: int):
    if repeats <= 0:
        print("Please enter a positive number for repeats.")
    else:
        for i in range(repeats):
            print(message)

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

# Ensures the main function is executed when the script runs
if __name__ == "__main__":
    main()
