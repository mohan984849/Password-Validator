SPECIAL_CHARS = "!@#$&*_"


def validate_password(password):

    errors = []

    # Length check
    if len(password) < 8:
        errors.append("Password must contain at least 8 characters.")

    elif len(password) > 16:
        errors.append("Password must not contain more than 16 characters.")

    # Empty password check
    if len(password) == 0:
        errors.append("Password cannot be empty.")
        return errors

    # First character check
    if not password[0].isupper():
        errors.append("Password must start with an uppercase letter.")

    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    for char in password:

        if char.isupper():
            has_uppercase = True

        elif char.islower():
            has_lowercase = True

        elif char.isdigit():
            has_number = True

        elif char in SPECIAL_CHARS:
            has_special = True

        elif char.isspace():
            errors.append("Password must not contain spaces.")

        else:
            errors.append(
                "Password contains an unsupported special character."
            )

    # Check required character types

    if not has_uppercase:
        errors.append("Password must contain at least one uppercase letter.")

    if not has_lowercase:
        errors.append("Password must contain at least one lowercase letter.")

    if not has_number:
        errors.append("Password must contain at least one number.")

    if not has_special:
        errors.append(
            "Password must contain at least one special character "
            "(! @ # $ & * _)."
        )

    return errors