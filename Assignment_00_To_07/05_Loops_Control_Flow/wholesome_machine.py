def main():
    affirmation = "I am capable of achieving anything I set my mind to."
    print(f"Kindly type the following affirmation: {affirmation}")

    while True:
        user_input = input("Please type: ")  # User input prompt
        if user_input == affirmation:
            print("Well done! You've typed it correctly. 👍")
            break
        else:
            print(f"Oops! That's not the affirmation. Try again: {affirmation}")


if __name__ == '__main__':
    main()
