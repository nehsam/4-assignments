# Speed of light ko constant variable me define karein
C = 299792458  # Speed of light in meters per second (m/s)

def main():
    """Einstein ka famous formula use karke mass ko energy me convert karein"""
    
    # User se mass ka input lena
    mass_in_kg = float(input("Mass (kg) enter karein: "))
    
    # Energy calculate karein using formula: E = m * C^2
    energy_in_joules = mass_in_kg * (C ** 2)
    
    # Result print karein
    print("\n=== Mass-Energy Conversion ===")
    print(f"Formula: E = m * C^2")
    print(f"Mass (m): {mass_in_kg} kg")
    print(f"Speed of Light (C): {C} m/s")
    print(f"Energy (E): {energy_in_joules:.2e} joules")  # Joules ko scientific notation me print karein

# Program run karne ke liye
if __name__ == '__main__':
    main()
