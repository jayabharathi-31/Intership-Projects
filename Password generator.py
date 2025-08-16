import random
import string

def generate_password():
    # Step 1: Input Handling
    try:
        length = int(input("Enter desired password length: ").strip())
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if length < 4:
        print("Password length should be at least 4 for good security.")
        return

    # Character options
    include_upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    include_lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
    include_digits = input("Include numbers? (y/n): ").strip().lower() == "y"
    include_special = input("Include special characters? (y/n): ").strip().lower() == "y"

    # Step 2: Prepare the character pool
    char_pool = ""
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation

    if not char_pool:
        print("No character types selected. Cannot generate password.")
        return

    # Step 3: Randomization
    password = "".join(random.choice(char_pool) for _ in range(length))

    # Step 4: Output the result
    print(f"\nGenerated Password: {password}")

# Run the program
generate_password()
