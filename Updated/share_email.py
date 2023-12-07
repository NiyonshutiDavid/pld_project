# share_email.py
import sqlite3

def share_email(username):
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()
    # Create a table to store user credentials
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS shared_emails (
        name TEXT NOT NULL,
        email TEXT NOT NULL PRIMARY KEY,
        shared TEXT NOT NULL
            )
        ''')

    # Prompt user for name and email details
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    # Ask user if they want to share the email
    share_choice = input("Do you want to share this email? (yes/no): ").lower()

    if share_choice == 'yes':
        # Add logic for sharing email
        shared ='1'
        cursor.execute("INSERT INTO shared_emails (name, email, shared) VALUES (?, ?, ?)",
                       (name, email, shared))
        conn.commit()
        print("Email shared successfully!")
    else:
        print("Email not shared.")

    conn.close()

# Example usage:
# In your main script, call share_email(username) where 'username' is the sender's username.
