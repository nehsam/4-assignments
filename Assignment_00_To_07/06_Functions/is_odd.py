def main():
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")
        
        if num % 5 == 0:
            print(f"{num} is a multiple of 5!")

if __name__ == '__main__':
    main()
