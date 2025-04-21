import random

def main():
    # User se input lene ka option (optional)
    n_numbers = int(input("How many random numbers do you want to generate?: "))
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))
    
    # Random numbers generate karna aur store karna
    random_numbers = [random.randint(min_value, max_value) for _ in range(n_numbers)]
    
    # Numbers print karna (comma-separated)
    print("Generated numbers:", ", ".join(map(str, random_numbers)))
    
    # Sum aur average calculate karna
    total_sum = sum(random_numbers)
    average = total_sum / n_numbers
    
    # Sum aur average print karna
    print(f"Sum of numbers: {total_sum}")
    print(f"Average of numbers: {average:.2f}")

if __name__ == '__main__':
    main()
