# This is a deliberately poorly implemented main script for a Library Management System.

from book_management import Book
import user_management
import checkout_management

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Search Book")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            Book(title, author, isbn).add()
            print("Book added.")
        elif choice == '2':
            Book.list_books()
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_management.add_user(name, user_id)
            print("User added.")
        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_management.checkout_book(user_id, isbn)
            print("Book checked out.")
        elif choice == '5':
            print("Enter the field value for your search. Press enter if the field is unknown\n")
            search_author = input("Author: ")
            search_title = input("Title: ")
            search_isbn = input("ISBN: ")
            book_obj.search(search_title, search_author, search_isbn)
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
