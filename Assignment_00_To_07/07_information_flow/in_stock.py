# Function to check the stock of a given fruit
def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "orange": 250,
        "mango": 700
    }
    return inventory.get(fruit.lower(), None)  # Return None if fruit is not found

def main():
    # Prompt the user for input
    fruit = input("Enter a fruit: ").strip()

    # Get the number of fruit in stock
    stock = num_in_stock(fruit)

    # Print appropriate message based on stock availability
    if stock is not None:
        print(f"This fruit is in stock! There are {stock} {fruit}s available.")
    else:
        print(f"Sorry, we do not have {fruit} in stock. Please check the spelling or try a different fruit.")

# Required line to run the program
if __name__ == '__main__':
    main()
