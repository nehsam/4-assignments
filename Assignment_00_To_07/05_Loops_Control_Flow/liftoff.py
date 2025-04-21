def main():
    # Countdown from 5 to 1, with a new twist
    for i in range(5, 0, -1):  # Starts from 5 and goes to 1
        print(f"Countdown: {i}", end=" | ")  # Print with prefix and separate values with "|"
    
    print("🚀 Launching Now!")  # A different message at the end

if __name__ == '__main__':
    main()
