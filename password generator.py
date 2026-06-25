# Random Password Generator
import secrets
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6 for security!"

    # character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|\;:,.<>?/~"

    # ensure password contains all types
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    
    all_chars =  digits + symbols + letters
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))

    # shuffle password
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

# user input
length = int(input("Enter password length: "))
print("Generated Secure Password:", generate_password(length))