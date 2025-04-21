import time  # Time module for delay

def main():
    # Loop 10 se 1 tak count karne ke liye
    for i in range(10, 0, -1):  # 10 se 1 tak reverse countdown
        print(i, end=" ", flush=True)  # Ek hi line me print karna
        time.sleep(1)  # 1-second ka delay
    
    # Jab countdown khatam ho, tab 'Liftoff!' print karna
    print("\nLiftoff!")  # Nayi line ke saath 'Liftoff!' dikhana

# Main function ko call karna
if __name__ == '__main__':
    main()
