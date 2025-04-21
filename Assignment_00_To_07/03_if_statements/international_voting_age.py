def check_voting_eligibility(age, country, voting_age):
    """Checks and prints voting eligibility for a specific country."""
    if age >= voting_age:
        print(f"You can vote in {country} where the voting age is {voting_age}.")
    else:
        print(f"You cannot vote in {country} where the voting age is {voting_age}.")

def main():
    # User se age input lena
    age = int(input("How old are you? "))

    # Har country ke liye voting eligibility check karna
    countries = [
        ("Peturksbouipo", 16),
        ("Stanlau", 25),
        ("Mayengua", 48),
    ]

    for country, voting_age in countries:
        check_voting_eligibility(age, country, voting_age)

# Program run karne ke liye zaroori line
if __name__ == '__main__':
    main()
