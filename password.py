import random
import string

def generate_password(length):
    # Define the possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print("=== Password Generator ===")
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = generate_password(length)
        print(f"\nYour generated password is:\n{password}")
except ValueError:
    print("Invalid input. Please enter a number.")
# === Sample Output ===
# Enter the desired password length: 8
# Your generated password is:
# dF7!k9@P
