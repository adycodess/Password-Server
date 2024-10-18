def view_password(username):
    with open_db() as db:
        if username not in db:
            print("User not found!")
            return

        # Ask for the passphrase to verify the user
        passphrase = getpass.getpass("Enter your passphrase to view your password: ")

        # Check if the passphrase matches the stored passphrase
        if passphrase == db[username]['passphrase']:
            # Display the stored password
            print(f"Your password is: {db[username]['password']}")
        else:
            print("Incorrect passphrase! Access denied.")
