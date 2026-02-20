import secrets
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

print("Welcome to the 🔐 PyPassword Generator!")

while True:
    try:
        length = int(input("Password length: "))

        if length > 0:
            break
        else:
            print("Password length must be greater than zero \nTry again!")
    
    except ValueError:
        print("Please enter a valid number.")

use_letters = input("Include letters? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()

pool = ""

if use_letters == "y":
    pool += letters

if use_symbols == "y":
    pool += symbols

if use_numbers == "y":
    pool += digits

if pool == "":
    print("You must select at least one character type.")
else:
    password_chars = []

    if use_letters == "y":
        password_chars.append(secrets.choice(letters))

    if use_symbols == "y":
        password_chars.append(secrets.choice(symbols))

    if use_numbers == "y":
        password_chars.append(secrets.choice(digits))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password_chars)

    password = "".join(password_chars)


    print(f"\nGenerated password: {password}")
