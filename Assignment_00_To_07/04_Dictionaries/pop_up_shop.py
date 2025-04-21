def main():
    # Dictionary storing fruit prices (per unit)
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 20.0,
        "kiwi": 2.5,
        "rambutan": 5.0,
        "mango": 7.0
    }

    total_cost = 0  # Initialize total cost
    receipt = []  # To store the receipt details

    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")
        
        cost = quantity * price  # Calculate cost for the current fruit
        total_cost += cost  # Add to total cost
        if quantity > 0:
            receipt.append(f"{fruit.capitalize()}: {quantity} x ${price:.2f} = ${cost:.2f}")

    # Print total cost
    print(f"\nYour total is ${total_cost:.2f}")

    # Ask user if they want to see the receipt
    show_receipt = input("Would you like to see the detailed receipt? (yes/no): ").strip().lower()
    if show_receipt in ["yes", "y"]:
        print("\nDetailed Receipt:")
        for item in receipt:
            print(item)

    print("\nThank you for shopping!")

# Required line to run the main() function
if __name__ == '__main__':
    main()
