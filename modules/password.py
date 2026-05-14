import random
import string

def generate_password():
    length = int(input("Length: "))

    chars = string.ascii_letters + string.digits + "!@#$%"

    password = "".join(random.choice(chars) for _ in range(length))

    print("Password:", password)
