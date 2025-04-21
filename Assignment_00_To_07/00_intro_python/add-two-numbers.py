def main():
     print("THIS PROGRAM ADD NUMBERS.")

try:
        # Prompt the user for input
        #input first number
        num1=int(input("Enter number 1:"))
        #input second number
        num2=int(input("Enter number 2:"))

       #adding
        total=num1+num2

       #this is output
        print(f"Total is {total}.")

except ValueError:
       print("invalid input.please enter a number.")


if __name__ == "__main__":
    main()     


