def main():
    print("THIS PROGRAM CONVERTS FAHRENHEIT TO CELSIUS.")

    # fahrenheit to celsius conversion

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celcius = (fahrenheit - 32) * 5 / 9

    print(f"{fahrenheit}Fahrenheit is {celcius:.2f}Celcius")

if __name__== '__main__':
     main()