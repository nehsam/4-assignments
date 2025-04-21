def main():
    # Planet gravity factors
    planet_gravity = {
        "Mercury": 0.376, "Venus": 0.889, "Mars": 0.378,
        "Jupiter": 2.36, "Saturn": 1.081, "Uranus": 0.815, "Neptune": 1.14
    }

    try:
        # User inputs
        earth_weight = float(input("Enter your weight on Earth: "))
        planet = input("Choose a planet (e.g., Mercury, Venus): ").title()

        # Calculate and display weight
        if planet in planet_gravity:
            print(f"Your weight on {planet} would be: {earth_weight * planet_gravity[planet]:.2f}")
        else:
            print("Invalid planet name. Please try again!")
    except ValueError:
        print("Please enter a valid numeric weight.")

if __name__ == "__main__":
    main()
