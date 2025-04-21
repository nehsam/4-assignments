# Function to get user data
def get_user_data():
    first_name = input("What is your first name?: ").strip()
    last_name = input("What is your last name?: ").strip()
    
    # Email validation
    while True:
        email = input("What is your email address?: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email. Please enter a valid email address.")
    
    return first_name, last_name, email  # Returning a tuple

def main():
    # Call the function and store the returned tuple
    user_data = get_user_data()
    
    # Display the collected data
    print("Received the following user data:")
    print(f"First Name: {user_data[0]}")
    print(f"Last Name: {user_data[1]}")
    print(f"Email: {user_data[2]}")

# Required line to run the program
if __name__ == '__main__':
    main()
