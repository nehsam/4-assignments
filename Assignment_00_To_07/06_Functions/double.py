def double(num):
    return num * 2

def main():
    while True:
        try:
            num = int(input("\033[94mEnter a number (or press Enter to stop): \033[0m"))
            result = double(num)
            print(f"Double that is {result}")
        except ValueError:
            print("\033[91mInvalid input, please enter a valid integer.\033[0m")
            continue

        # Option to continue or stop
        cont = input("Do you want to double another number? (yes/no): ")
        if cont.lower() != 'yes':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()
