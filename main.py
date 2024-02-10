# This is a deliberately poorly implemented main script for a Library Management System.

from book import Book
from library import Library
import user
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
            book = Book(title, author, isbn)
            Library.add_book(book)
            print("Book added.")

        elif choice == '2':
            Library.list_all_books()

        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user.add_user(name, user_id)
            print("User added.")

        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_management.checkout_book(user_id, isbn)
            print("Book checked out.")

        elif choice == '5':
            print("Enter the field with which you want to search\n")
            print("1. Title")
            print("2. Author")
            print("3. ISBN")
            choice = input("Enter choice: ")
            if choice == '1':
                search_field = "title"
                search_query = input("Title: ")
            elif choice == '2':
                search_field = "author"
                search_query = input("Author: ")
            elif choice == '3':
                search_field = "isbn"
                search_query = input("ISBN: ")
            else:
                print("Invalid choice, please try again.")
                continue
            Library.search_book(search_field, search_query)
            print ("Search Completed")

        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")
            

if __name__ == "__main__":
    main()
