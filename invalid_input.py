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