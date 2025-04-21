def main():
    print("THIS PROGRAM CALCULATES THE PRICE OF SUBJECTS.")

    # subjects = ["Math", "Science", "History", "English", "Urdu", "Computer Science", "Biology"]
    # price of each subject
    math = 50

    science = math + 20

    history = science * 2

    english = history / 3

    urdu = english + 100

    computer_science = urdu - 50

    biology = computer_science * 2

    print("math is " + str(math))
    print("science is " + str(science))
    print("history is " + str(history))
    print("english is " + str(english))
    print("urdu is " + str(urdu))
    print("computer science is " + str(computer_science))
    print("biology is " + str(biology))

if __name__ == '__main__':
    main()    