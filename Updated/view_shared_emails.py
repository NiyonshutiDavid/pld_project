# view_shared_emails.py
import sqlite3

def view_shared_emails(username):
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()

    # Retrieve shared emails from the database, excluding the user
    cursor.execute("SELECT name, email FROM shared_emails WHERE name != ? AND shared = 1", (username,))
    shared_emails = cursor.fetchall()

    if shared_emails:
        print("People who have shared their emails and allowed to see shared emails:")
        for name, email in shared_emails:
            print(f"{name}, email: {email}")
    else:
        print("No shared emails found from others who have shared theirs.")

    conn.close()

# Example usage:
# In your main script, call view_shared_emails(username) where 'username' is the viewer's username.
