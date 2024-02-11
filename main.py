"""
Library Management System Main Script

Author: Kunal Kundu
Date: Feb 10,2024

Description: 
This script is the main interface for a Library Management System, handling book and user management tasks 
like additions, listings, and checkouts. Designed for modularity, it separates entities and processes into distinct 
modules for easy expansion and maintenance, ensuring adaptability for future enhancements.

Design Comments:
- The system uses a straightforward, menu-driven interface for interaction, ensuring ease of use.
- It demonstrates basic principles of object-oriented design, with classes representing key entities and operations.
"""


from book import Book
from library import Library
from user import User
from input_validation import input_title, input_author, input_isbn, input_quantity, input_user_name, input_user_id


def main_menu():
    """
    @summary: Displays the main menu and captures user choice.
    @return(str): The user's choice as a string.
    """
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
    """
    @summary: Main application loop, processing user inputs and executing corresponding actions.
    """
    while True:
        choice = main_menu()

        # Add a new book to the library collection
        if choice == '1':
            title = input_title()
            author = input_author()
            isbn = input_isbn()
            quantity = input_quantity()
            book = Book(title, author, isbn, quantity)
            Library.add_book(book)
            print("Book added.")
            
        # List all books in the library
        elif choice == '2':
            Library.list_all_books()

        # Add a new user to the library system
        elif choice == '3':
            name = input_user_name()
            user_id = input_user_id()
            user = User(name, user_id)
            Library.add_user(user)
            print("User added.")

        # List all the users
        elif choice == '4':
            Library.list_all_users()

        # Borrow book
        elif choice == '5':
            user_id = input_user_id()
            isbn = input_isbn()
            Library.checkin_book(user_id, isbn)

        # checkout book
        elif choice == '6':
            user_id = input_user_id()
            isbn = input_isbn()
            Library.checkout_book(user_id, isbn)

        # Search operation on book
        elif choice == '7':
            print("Enter the field with which you want to search\n")
            print("1. Title")
            print("2. Author")
            print("3. ISBN")
            choice = input("Enter choice: ")
            if choice == '1':
                search_field = "title"
                search_query = input_title()
            elif choice == '2':
                search_field = "author"
                search_query = input_author()
            elif choice == '3':
                search_field = "isbn"
                search_query = input_isbn()
            else:
                print("Invalid choice, please try again.")
                continue
            Library.search_book(search_field, search_query)
            print("\nSearch completed.")

        # Update the book
        elif choice == '8':
            isbn = input_isbn()
            Library.update_book(isbn)

        # Delete operation on book
        elif choice == '9':
            print("Enter the field with which you want to delete a book\n")
            print("1. Title")
            print("2. Author")
            print("3. ISBN")
            choice = input("Enter choice: ")
            if choice == '1':
                search_field = "title"
                search_query = input_title()
            elif choice == '2':
                search_field = "author"
                search_query = input_author()
            elif choice == '3':
                search_field = "isbn"
                search_query = input_isbn()
            else:
                print("Invalid choice, please try again.")
                continue
            Library.delete_book(search_field, search_query)

        # Search operation on users
        elif choice == '10':
            print("Enter the field with which you want to search\n")
            print("1. Name")
            print("2. User ID")
            choice = input("Enter choice: ")
            if choice == '1':
                search_field = "name"
                search_query = input_user_name()
            elif choice == '2':
                search_field = "userId"
                search_query = input_user_id()
            else:
                print("Invalid choice, please try again.")
                continue
            Library.search_user(search_field, search_query)
            print("\nSearch completed.")

        # Update operation on user
        elif choice == '11':
            user_id = input_user_id()
            Library.update_user(user_id)

        # Delete operation on user
        elif choice == '12':
            print("Enter the field with which you want to delete a user\n")
            print("1. Name")
            print("2. User ID")
            choice = input("Enter choice: ")
            if choice == '1':
                search_field = "name"
                search_query = input_user_name()
            elif choice == '2':
                search_field = "userId"
                search_query = input_user_id()
            else:
                print("Invalid choice, please try again.")
                continue
            Library.delete_user(search_field, search_query)

        # Exit from the tool
        elif choice == '13':
            print("Exiting.")
            break
        
        # Handle invalid operation
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
