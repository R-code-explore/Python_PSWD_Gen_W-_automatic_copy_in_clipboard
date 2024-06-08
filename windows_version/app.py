import secrets
import string
import pyperclip

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = secrets.choice([10, 11, 12])
    password = generate_password(password_length)
    pyperclip.copy(password)
    print(f"Your generated password is: {password}")
    print("The password has been copied to your clipboard.")
    input("Press Enter to exit...")