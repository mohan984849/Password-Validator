from password_validator import validate_password


def main():

    print("=" * 50)
    print("             PASSWORD VALIDATOR")
    print("=" * 50)

    print("\nPassword Requirements:")
    print("- Length: 8 to 16 characters")
    print("- Must start with an uppercase letter")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one number")
    print("- At least one special character: ! @ # $ & * _")
    print("- No spaces")
    print("- No unsupported characters")

    while True:

        password = input("\nEnter your password: ")

        errors = validate_password(password)

        print("\n" + "-" * 50)

        if len(errors) == 0:

            print("✅ VALID PASSWORD")
            print("Your password satisfies all requirements.")

        else:

            print("❌ INVALID PASSWORD")
            print("\nReasons:")

            for error in errors:
                print("❌", error)

        print("-" * 50)

        choice = input(
            "\nDo you want to check another password? (yes/no): "
        )

        choice = choice.strip().lower()

        if choice != "yes":
            print("\nThank you for using Password Validator!")
            break


if __name__ == "__main__":
    main()