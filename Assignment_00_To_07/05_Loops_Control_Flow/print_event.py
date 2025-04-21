def main():
    count = 20  # Number of even numbers to print
    even_numbers = [i * 2 for i in range(count)]  # List comprehension to generate even numbers
    print(*even_numbers)  # Print the list of even numbers space-separated

if __name__ == '__main__':
    main()
