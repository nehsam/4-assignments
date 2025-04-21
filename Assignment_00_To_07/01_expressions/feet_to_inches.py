# Feet to Inches Converter Program

# Constant for conversion factor
INCHES_IN_FOOT = 12  # 1 foot = 12 inches

def main():
    # User se feet ka input lena
    feet = float(input("Kitne feet ko inches me convert karna hai? "))
    
    # Feet ko inches me convert karna
    inches = feet * INCHES_IN_FOOT
    
    # Result display karna
    print(f"{feet} feet ka equivalent hai {inches} inches.")
    
# Main function call
if __name__ == '__main__':
    main()
