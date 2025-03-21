import random
import string

import pyperclip


def generate_password(length, use_uppercase, use_numbers, use_symbols):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = lower + upper + numbers + symbols

    if not all_chars:
        return "Error: Select at least one character type."

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = generate_password(length, use_uppercase, use_numbers, use_symbols)
print(f"Generated Password: " + password)
pyperclip.copy(password)
print("Password copied to clipboard!")
