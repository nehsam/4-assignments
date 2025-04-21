def main():
    print("THIS PROGRAM CALCULATES THE PERIMETER OF A TRIANGLE.")
    # Prompt the user for the lengths of the sides of the triangle
    
    side1 = float(input("Enter the length of side 1: "))

    side2 = float(input("Enter the length of side 2: "))

    side3 = float(input("Enter the length of side 3: "))

    perimeter =  side1 + side2 + side3
    # Calculate the perimeter of the triangle
    print(f"The perimeter of the triangle is: {perimeter}")

if __name__ == "__main__":
    main() 

