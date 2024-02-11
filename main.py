# This is a deliberately poorly implemented main script for a Library Management System.

from book import Book
from library import Library
from user import User


def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkin (Borrow) Book")
    print("6. Checkout (Return) Book")
    print("7. Search Book")
    print("8. Update Book")
    print("9. Delete Book")
    print("10. Search User")
    print("11. Update User")
    print("12. Delete User")
    print("13. Exit")
    choice = input("Enter choice: ")
    return choice


def main():
    while True:
        choice = main_menu()

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            quantity = input("Enter Quantity: ")
            book = Book(title, author, isbn, quantity)
            Library.add_book(book)
            print("Book added.")

        elif choice == '2':
            Library.list_all_books()

        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user = User(name, user_id)
            Library.add_user(user)
            print("User added.")

        elif choice == '4':
            Library.list_all_users()

        elif choice == '5':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkin (Borrow): ")
            Library.checkin_book(user_id, isbn)

        elif choice == '6':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout (Issue): ")
            Library.checkout_book(user_id, isbn)

        elif choice == '7':
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
            print("\nSearch completed.")

        elif choice == '8':
            isbn = input("Enter ISBN of the book to update: ")
            Library.update_book(isbn)

        elif choice == '9':
            print("Enter the field with which you want to delete a book\n")
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
            Library.delete_book(search_field, search_query)

        elif choice == '10':
            print("Enter the field with which you want to search\n")
            print("1. Name")
            print("2. User ID")
            choice = input("Enter choice: ")
            if choice == '1':
                search_field = "name"
                search_query = input("Name: ")
            elif choice == '2':
                search_field = "userId"
                search_query = input("User ID: ")
            else:
                print("Invalid choice, please try again.")
                continue
            Library.search_user(search_field, search_query)
            print("\nSearch completed.")

        elif choice == '11':
            user_id = input("Enter User ID of the user to update: ")
            Library.update_user(user_id)

        elif choice == '12':
            print("Enter the field with which you want to delete a user\n")
            print("1. Name")
            print("2. User ID")
            choice = input("Enter choice: ")
            if choice == '1':
                search_field = "name"
                search_query = input("Name: ")
            elif choice == '2':
                search_field = "userId"
                search_query = input("User ID: ")
            else:
                print("Invalid choice, please try again.")
                continue
            Library.delete_user(search_field, search_query)

        elif choice == '13':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
