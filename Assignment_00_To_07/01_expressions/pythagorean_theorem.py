# Right Triangle Hypotenuse Calculator

import math  # Square root ke liye math library import

def main():
    # User se input lena for both sides
    ab = float(input("AB ki length enter karein: "))
    ac = float(input("AC ki length enter karein: "))
    
    # Hypotenuse calculate karna
    bc = math.sqrt(ab**2 + ac**2)
    
    # Result print karna
    print(f"Triangle ka hypotenuse (BC) hai: {bc}")
    
# Main function call
if __name__ == '__main__':
    main()
