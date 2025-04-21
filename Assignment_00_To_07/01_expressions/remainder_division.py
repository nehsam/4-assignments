# Division aur Remainder Calculator

def main():
    # User se input lena for dividend aur divisor
    dividend = int(input("Ek integer number likhiye jo divide hoga: "))
    divisor = int(input("Ek integer number likhiye jo divide karega: "))
    
    # Integer division aur remainder nikalna
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Result display karna
    print(f"Result: {quotient}, aur remainder: {remainder}")
    

# Main function call
if __name__ == '__main__':
    main()
