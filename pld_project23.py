import re

def welcome_message():
    return "Welcome to the Entrepreneurship Incubator! Choose an option below to get started:"

def main_menu():
    print("1. Register")
    print("2. Share Email")
    print("3. Access Resources")
    print("4. View Shared Emails")
    print("5. Exit")

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

    print("\nThank you for registering, {}. Your information has been stored.".format(name))

    global shared_emails
    shared_emails[name] = email

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    else:
        return False

def share_email():
    global shared_emails
    if not shared_emails:
        print("\nNo shared emails found.")
    else:
        print("\nShared Emails:")
        for name, email in shared_emails.items():
            print(f"{name}: {email}")

def access_resources():
    print("\nSelect a resource type:")
    print("1. Articles")
    print("2. Videos")
    print("3. Blogs")

    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        print("\nHere are some articles to help you improve your entrepreneurial skills:")
        print("1. Top 10 Tips for Starting a Business - [Link]")
        print("2. Navigating the Startup Ecosystem - [Link]")

        choice = input("Enter your choice (1-2): ")
        if choice == '1':
            print("\nArticle: Top 10 Tips for Starting a Business")
            print("[Content of the article]")

def view_shared_emails():
    global shared_emails
    if not shared_emails:
        print("\nNo shared emails found.")
    else:
        print("\nShared Emails:")
        for name, email in shared_emails.items():
            print(f"{name}: {email}")

def exit_program():
    print("\nGoodbye! Thank you for using the Entrepreneurship Incubator.")

def invalid_input():
    print("Invalid input. Please enter a valid option.")

shared_emails = {}
user_data = {}

print(welcome_message())
while True:
    main_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        register()
    elif choice == '2':
        share_email()
    elif choice == '3':
        access_resources()
    elif choice == '4':
        view_shared_emails()
    elif choice == '5':
        exit_program()
        break
    else:
        invalid_input()
