import random

def done(probability):
    """Returns True with the given probability"""
    return random.random() < probability

def chaotic_counting(done_likelihood):
    """Counts from 1 to 10, but stops early if done() returns True"""
    for i in range(1, 11):
        if done(done_likelihood):
            print(f"\nStopped early at {i}.")
            return  # Stop execution and return to main()
        print(i, end=" ")

def main():
    # User se DONE_LIKELIHOOD ka input lena
    user_input = input("Enter a probability for stopping (0 to 1): ")
    try:
        done_likelihood = float(user_input)
        if done_likelihood < 0 or done_likelihood > 1:
            print("Invalid probability. Using default 0.2.")
            done_likelihood = 0.2
    except ValueError:
        print("Invalid input. Using default 0.2.")
        done_likelihood = 0.2

    print(f"I'm going to count until 10 or until I feel like stopping, with a {done_likelihood} chance of stopping.")
    chaotic_counting(done_likelihood)
    print("\nI'm done.")

if __name__ == '__main__':
    main()
