def read_phone_numbers():
    phonebook = {}

    print("Enter name and phone number. Press Enter without typing a name to stop.")
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        number = input("Number: ").strip()

        # Validate number
        if not number.isdigit():
            print("Invalid number! Please enter digits only.")
            continue

        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    if not phonebook:
        print("\nPhonebook is empty. No entries to display.")
        return

    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_number(phonebook):
    if not phonebook:
        print("\nPhonebook is empty. Add some entries first.")
        return

    print("\nLookup Phone Number:")
    while True:
        name = input("Enter name to lookup (or press Enter to stop): ").strip()
        if name == "":
            break

        # Case-insensitive lookup
        found = {key: value for key, value in phonebook.items() if key.lower() == name.lower()}
        if not found:
            print(f"{name} is not in the phonebook.")
        else:
            for key, value in found.items():
                print(f"{key} -> {value}")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_number(phonebook)


if __name__ == '__main__':
    main()
