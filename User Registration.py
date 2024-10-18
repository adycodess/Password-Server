def register_user(username):
  '''Criteria for a Strong Password:
    At least has 8 characters
    At least has one uppercase letter
    At least has one lowercase letter
    At least has one number
    At least has one special character'''

    # Ask user to choose between creating a password or generating a random one
    choice = int(input(''' 1. Create a Password
2. Generate a Random Password
Choose an option: '''))

    if choice == 1:
        while True:
            password = getpass.getpass("Enter your password: ")
            errors = check_password(password)

            if not errors:
                print("Password accepted!")
                break
            else:
                print("Password does not meet the following criteria:")
                for error in errors:
                    print(error)

    elif choice == 2:
        length = int(input("Enter the desired length of the password (between 8 and 20): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")

    else:
        print("Invalid choice.")
        return

    passphrase = getpass.getpass("Set a passphrase for viewing your password: ")

    # Store the password and passphrase in the shelve database
    with open_db() as db:
        db[username] = {'password': password, 'passphrase': passphrase}

    print(f"User '{username}' registered successfully!")

