"""
Calculate the total number of seconds for a given number of years using constants.
"""

# Constants for time calculations
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def main():
    # Ask the user for the number of years
    years = int(input("Enter the number of years to calculate seconds for: "))
    
    # Formula to calculate total seconds for the given number of years
    total_seconds = years * DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Display the result in a user-friendly way
    print(f"There are {total_seconds} seconds in {years} year(s)! 🎉")


# Required line to run the program
if __name__ == '__main__':
    main()
