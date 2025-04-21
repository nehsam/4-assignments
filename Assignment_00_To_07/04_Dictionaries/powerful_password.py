import hashlib
import os

def hash_password(password, salt=None):
    """
    Returns the SHA-256 hash of the given password concatenated with a salt.
    Generates a new salt if not provided.
    """
    if salt is None:
        salt = os.urandom(16)  # Generate a random 16-byte salt
    password_salt_combo = password.encode() + salt
    hashed_password = hashlib.sha256(password_salt_combo).hexdigest()
    return hashed_password, salt

def login(email, password_to_check, stored_logins):
    """
    Checks if the given email's stored password hash matches the hash of the password_to_check.
    Returns True if the login is successful, else False.
    """
    email = email.lower()  # Make email case-insensitive
    if email in stored_logins:  # Check if email exists
        stored_hash, salt = stored_logins[email]  # Get stored hash and salt
        check_hash, _ = hash_password(password_to_check, salt)  # Rehash with the same salt
        return stored_hash == check_hash  # Compare hashes
    return False

def main():
    # Stored logins (email: (hashed password, salt))
    stored_logins = {
        "user@example.com": hash_password("securepassword123"),
        "zehra@dev.com": hash_password("mysecretpass"),
    }

    # User input
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check login
    if login(email, password, stored_logins):
        print("Login successful! ✅")
    else:
        print("Login failed! ❌ Incorrect email or password.")

# Required line to run the main() function
if __name__ == '__main__':
    main()
