import random
import string

# Function to generate a random strong password
def generate_password(length):
    # Defines all the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly selects characters to form the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Asks the user to input the length of the password they desire
password_length = int(input("Enter the desired password length (number > 7): "))

# Checks if password length is less than 7
if password_length < 7:
    print("Password length is too short to create a strong password. Password length must be at least 7 characters.")
else:
    # Generates and prints the random password
    password = generate_password(password_length)
    print(f"Your generated password is: {password}")
