import sqlite3
from share_email import share_email
from access_resources import access_resources
from view_shared_emails import view_shared_emails




# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_credentials.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the shared_startups table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shared_startups (
        name TEXT NOT NULL,
        email TEXT NOT NULL PRIMARY KEY,
        title TEXT NOT NULL,
        goal TEXT NOT NULL,
        entrepreneur TEXT NOT NULL
    )
''')


# Create a table to store user credentials
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL PRIMARY KEY,
        password TEXT NOT NULL,
        user_type TEXT CHECK (user_type IN ('Entrepreneur', 'Investor')) NOT NULL
    )
''')

# Function to register a new user
def register_user(username, password, user_type):
    # Check if the username already exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    if cursor.fetchone() is not None:
        print("Username already exists. Please choose a different one.")
    else:
        # If username doesn't exist, insert the new user
        cursor.execute('INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)', (username, password, user_type))
        conn.commit()
        print("Registration successful! Please login.")

# Function to check if the entered credentials are valid
def check_credentials(username, password):
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    return cursor.fetchone()

# Function to prompt user for login or registration
def login_or_register():
    while True:
        print("***********************************************")
        print("*****Welcome to Entrepreneurship Incubator*****")
        print("***********************************************")
        print("1. Login >>>>>>>")
        print("2. Register ++++")
        print("3. Exit --------")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("1. Login as Entrepreneur")
            print("2. Login as Investor")
            print("3. Back to main menu")
            print("4. Exit")
            magic = int(input("Enter your choice: "))
            if magic == 1:
                user_type = 'Entrepreneur'
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                user = check_credentials(username, password)
                if user and user[2] == user_type:
                    print("Welcome, {}! You are logged in as an Entrepreneur.".format(username))
                    main_menu_entrepreneur(username)
                else:
                    print("Invalid credentials. Please try again.")
            elif magic == 2:
                user_type = 'Investor'
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                user = check_credentials(username, password)
                if user and user[2] == user_type:
                    print("Welcome, {}! You are logged in as an Investor.".format(username))
                    # Add logic for investor menu if needed
                    main_menu_investor(username)
                else:
                    print("Invalid credentials. Please try again.")
            elif magic == 3:
                # Go back to the main menu
                continue
            elif magic == 4:
                # Exit the program
                break
            else:
                print("Invalid choice. Please try again.")
        elif choice == 2:
            print("1. Register as Entrepreneur")
            print("2. Register as Investor")
            print("3. Back to main menu")
            print("4. Exit")
            register_choice = int(input("Enter your choice: "))
            if register_choice == 1:
                user_type = 'Entrepreneur'
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                register_user(username, password, user_type)
            elif register_choice == 2:
                user_type = 'Investor'
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                register_user(username, password, user_type)
            elif register_choice == 3:
                # Going back to the main menu
                continue
            elif register_choice == 4:
                # Exiting the program
                print("Bye!!!!!!!!!!!!!!")
                break
            else:
                print("Invalid choice. Please try again.")
        elif choice == 3:
            # Exit the program
            print("GoodBye !!!!!!!!!!")
            print("Exiting the programm .............")
            break
        else:
            print("Invalid choice. Please try again.")

# Function for start up sharing
def share_startup(username):
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()

    # Prompt entrepreneur for startup information
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    title = input("Enter the title of your startup: ")
    goal = input("Enter the goal of your startup: ")

    # Share the startup information
    cursor.execute("INSERT INTO shared_startups (name, email, title, goal, entrepreneur) VALUES (?, ?, ?, ?, ?)",
                   (name, email, title, goal, username))
    conn.commit()
    print("Startup information shared successfully!")

    conn.close()


# Function for the entrepreneur main menu
def main_menu_entrepreneur(username):
    while True:
        print("\nEntrepreneur Main Menu")
        print("1. Share Email")
        print("2. Access Resources")
        print("3. View Shared Emails")
        print("4. Share your start up")
        print("5. Logout")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # Add logic for sharing email
            print("Welcome to Share Email page")
            share_email(username)
        elif choice == 2:
            # Add logic for accessing resources
            print("Welcome to Access Resources page")
            access_resources(username)
        elif choice == 3:
            # Add logic for viewing shared emails
            print("Welcome to  View Shared Emails page")
            view_shared_emails(username)
        elif choice == 4:
            share_startup(username)
        elif choice == 5:
            print("Logging out...")
            break
        elif choice == 6:
            print("Exiting the program...")
            exit()
        else:
            print("Invalid choice. Please try again.")



def view_entrepreneurs_emails():
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()

    # Retrieve shared emails from entrepreneurs
    cursor.execute("SELECT name, email FROM shared_emails WHERE shared = 1")
    shared_emails = cursor.fetchall()

    if shared_emails:
        print("Entrepreneurs who have shared their emails:")
        for name, email in shared_emails:
            print(f"{name}, email: {email}")
    else:
        print("No shared emails found from entrepreneurs.")

    conn.close()

def access_available_startups():
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()

    # Retrieve information about available startups
    cursor.execute('''SELECT name, email, title, goal FROM shared_startups''')
    startups = cursor.fetchall()

    if startups:
        print("Available Startups:")
        for startup in startups:
            print(f"***Founder: {startup[0]} - Contacts: {startup[1]} - Start up Title: {startup[2]} - Goal: {startup[3]}")
    else:
        print("No information available about startups.")

    conn.close()

# Function to handle logout
def logout():
    print("Logging out from Investor Page.")

def main_menu_investor(username):
    while True:
        print("Welcome to Investor Page")
        print("1. View Entrepreneurs' Shared Emails")
        print("2. Access Entrepreneurs' Resources")
        print("3. Access Available Startups")
        print("4. Logout")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_entrepreneurs_emails()
        elif choice == 2:
            access_resources(username)
        elif choice == 3:
            access_available_startups()
        elif choice == 4:
            logout()
            break
        else:
            print("Invalid choice. Please try again.")


# Execute the login or register function
login_or_register()

# Close the database connection
conn.close()
