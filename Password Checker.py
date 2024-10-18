def check_password(password):
    """
    Checks if the password meets the specified criteria.
    """
    errors = []
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()_+=[\\]{};':\"|,.<>/?":
            has_special = True

    if not has_lower:
        errors.append("Password must contain at least one lowercase letter.")
    if not has_upper:
        errors.append("Password must contain at least one uppercase letter.")
    if not has_digit:
        errors.append("Password must contain at least one number.")
    if not has_special:
        errors.append("Password must contain at least one special character.")

    return errors

