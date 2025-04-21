def main():
    # User se input lena
    person_name = input("Who is your favorite person? ")
    relation = input("What is your relation with them? (mom, dad, sister, brother, friend, love): ").lower()

    # Har relation ke liye funny aur interesting sentences create karna
    if relation == "friend":
        print(f"\nOh, your friend {person_name}? You know, they are always the last one to leave the party, and they still can't find their keys!")
    elif relation == "mom":
        print(f"\nYour mom {person_name}? Haha, she's probably already mad at you for something, right? She always gets angry over the smallest things!")
    elif relation == "dad":
        print(f"\nYour dad {person_name}? He's the one who always has some serious life advice for you, even if you never asked for it!")
    elif relation == "sister":
        print(f"\nYour sister {person_name}? She'll probably steal your clothes and then tell you, 'You don't even wear this anymore!'")
    elif relation == "brother":
        print(f"\nYour brother {person_name}? He's the type who'd eat all your snacks and then pretend like it wasn't him!")
    elif relation == "love":
        print(f"\nYour love {person_name}? Aww, they must be the kind of person who always surprises you with random gifts and makes you smile even on your worst days!")
    else:
        print("\nHmm, looks like the relation isn't recognized! Let's stick to 'family' vibes for now.")

# Program ko run karne ke liye
if __name__ == '__main__':
    main()
