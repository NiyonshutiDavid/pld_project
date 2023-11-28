def view_shared_emails():
    global shared_emails
    if not shared_emails:
        print("\nNo shared emails found.")
    else:
        print("\nShared Emails:")
        for name, email in shared_emails.items():
            print(f"{name}: {email}"))
