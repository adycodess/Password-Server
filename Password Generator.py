def generate_password(length):
    """
    Generates a random password with at least one uppercase, lowercase, digit, and special character.
    """
    while length < 8 or length > 20:
        print("Length must be between 8 and 20 characters")
        length = int(input("Enter the desired length of the password: "))

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*()_+=[\\]{};':\"|,.<>/?"

    # Ensure at least one of each character type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password with random characters
    while len(password) < length:
        password.append(random.choice(lower + upper + digits + special))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Join the list into a string
    return ''.join(password)

