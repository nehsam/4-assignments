def is_leap_year(year):
    """Checks if a given year is a leap year."""
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def main():
    # User se input lena
    year = int(input("Please input a year: "))

    # Leap year check karna
    if is_leap_year(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Program run karne ke liye zaroori line
if __name__ == '__main__':
    main()
