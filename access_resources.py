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

    elif choice == '2':
        
