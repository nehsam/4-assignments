def main():
    while True:
        # User se height input lena
        height = input("How tall are you (in cm)? (Press Enter to exit): ")

        # Agar user ne khali enter press kiya to program stop ho jaye
        if not height.strip():
            print("Exiting the program. Have a great day!")
            break

        # Input validation aur height ko number me convert karna
        try:
            height = int(height)
        except ValueError:
            print("Please enter a valid number for height.\n")
            continue

        # Height check karna
        if height >= 50:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")

# Program ko run karne ke liye zaroori line
if __name__ == '__main__':
    main()
