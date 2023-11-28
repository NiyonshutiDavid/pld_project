from welcome_message import welcome_message
from main_menu import main_menu
from register import register
from login import login
from share_email import share_email
from access_resources import access_resources
from view_shared_emails import view_shared_emails
from exit_program import exit_program
from invalid_input import invalid_input

shared_emails = {}
user_data = {}

print(welcome_message())
while True:
    main_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        share_email()
    elif choice == '4':
        access_resources()
    elif choice == '5':
        view_shared_emails()
    elif choice == '6':
        exit_program()
        break
    else:
        invalid_input()
