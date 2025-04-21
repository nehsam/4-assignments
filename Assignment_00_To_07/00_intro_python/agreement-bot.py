def main():
    print("THIS PROGRAM ASKS FOR YOUR FAVORITE SUBJECT.")
    try:
        question = input("What is your favorite subject?")
        print(f"My favorite subject is {question}.")
    except ValueError:
        print("Invalid input. Please enter a valid answer.")

if __name__ == '__main__':
    # Call the main function to start the program
    main()



    
