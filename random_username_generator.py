import random
import string

def generate_username(include_numbers=True, include_special_chars=False):
    adjectives = ["Cool", "Happy", "Smart", "Funny", "Brave", "Witty"]
    nouns = ["Tiger", "Ninja", "Pirate", "Wizard", "Knight", "Samurai"]

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    username = adjective + noun

    if include_numbers:
        username += str(random.randint(10, 999))

    if include_special_chars:
        special_chars = '!@#$%^&*()'
        username += random.choice(special_chars)

    return username

def save_username(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")

def main():
    print("Welcome to the Random Username Generator!")

    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    username = generate_username(include_numbers, include_special_chars)
    print(f"Generated Username: {username}")

    save = input("Do you want to save this username? (yes/no): ").strip().lower()
    if save == "yes":
        save_username(username)
        print("Username saved to usernames.txt!")
    else:
        print("Username not saved.")

if __name__ == "__main__":
    main()
