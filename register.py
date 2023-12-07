def register():
    global user_data
    user_data = {}

    name = input("Enter your name: ")
    user_data['name'] = name

    email = input("Enter your email: ")
    user_data['email'] = email

    phone = input("Enter your phone number: ")
    user_data['phone'] = phone

    if not validate_email(email):
        print("\nInvalid email. Please register again.")
        return

      permission = input("Do you give permission to share your email? (yes/no): ").lower()
    if permission == 'yes':
        print("\nThank you for registering, {}. Your information has been stored.".format(name))
        global shared_emails
        shared_emails[name] = email
    else:
        print("\nPermission denied. Your information has not been shared.")


    global shared_emails
    shared_emails[name] = email

