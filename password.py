import string
import random
import argparse

# Function to generate the password
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    # Default characters include lowercase letters
    characters = string.ascii_lowercase

    # Add other character types based on user's choice
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main function to parse arguments and generate the password
def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Generate a secure random password.')
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-lo', '--lowercase', action='store_true', help='Include lowercase letters')
    parser.add_argument('-d', '--digits', action='store_true', help='Include digits')
    parser.add_argument('-s', '--special', action='store_true', help='Include special characters')

    # Parse arguments
    args = parser.parse_args()

    # Generate the password
    new_password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special)
    print(f"Your new password is: {new_password}")

main()

