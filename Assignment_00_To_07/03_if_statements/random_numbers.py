import random  # Random module import karna

def main():
    # User se number of random numbers generate karne ka input lena
    count = int(input("How many random numbers do you want to generate? "))
    random_numbers = [random.randint(1, 100) for _ in range(count)]  # Random numbers ki list
    print("Generated Random Numbers:", *random_numbers)  # Random numbers print karna

# Program ko run karne ke liye zaroori line
if __name__ == '__main__':
    main()
