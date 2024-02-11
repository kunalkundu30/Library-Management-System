import storage
from book import Book
from user import User
from utils import get_configuration_file_location, get_configuration_file
from datetime import date


class Library:

    @staticmethod
    def add_book(book):
        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        book_file_path = config["book_file_path"]
        storage.store(book, book_file_path)

    @staticmethod
    def list_all_books():
        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        book_file_path = config["book_file_path"]

        books_dict = storage.retrieve(book_file_path)

        if books_dict:
            keys = list(books_dict.keys())
            length = len(books_dict[keys[0]])
            books_list = [
                [books_dict[key][index] for key in keys] for index in range(length)
            ]
            for book in books_list:
                print(
                    "\nTitle: {}, Author: {}, ISBN: {}".format(
                        book[0], book[1], book[2]
                    )
                )
        else:
            print("\nNo books in library")

    @staticmethod
    def search_book(search_field, search_query, should_return = False, stock_check_checkin=False, stock_check_checkout=False):
        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        book_file_path = config["book_file_path"]

        books_dict = storage.retrieve(book_file_path)
        indices = []
        if books_dict:
            for index, value in enumerate(books_dict[search_field]):
                if search_query == value:
                    indices.append(index)
            if len(indices) == 0:
                print("\nSearch result is empty. Search term not found.")
            else:
                print("\nThe search result(s) are:")
                for index in indices:
                    print(
                        "\nTitle: {}, Author: {}, ISBN: {}".format(
                            books_dict["title"][index],
                            books_dict["author"][index],
                            books_dict["isbn"][index],
                        )
                    )
        else:
            print("\nNo books in library")
        if should_return == True:
            return (indices)
        elif stock_check_checkin == True:
            if int(books_dict["copies"][indices[0]]) > int(books_dict["borrowed"][indices[0]]):
                return (indices, 'Y')
            else:
                return (indices, 'N')
        elif stock_check_checkout == True:
            if int(books_dict["borrowed"][indices[0]]) > 0:
                return (indices, 'Y')
            else:
                return (indices, 'N')


    @staticmethod
    def delete_book(search_field, search_query):
        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        book_file_path = config["book_file_path"]

        delete_indices = Library.search_book(search_field, search_query, should_return = True)
        delete_indices = [index+1 for index in delete_indices]
        if len(delete_indices)>0:
            print("\nThese books will be deleted. Do you wish to continue?")
            choice = input("Enter Y/N: ")
            if choice == "Y":
                storage.delete(delete_indices, book_file_path)
                print("\nDeleted successfully.")
            elif choice == "N":
                print("\nDeletion task aborted")
            else:
                print("\nInvalid choice, please try again.")
        else:
            print("\nBook not found. Deletion task aborted.")

    @staticmethod
    def update_book(isbn):
        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        book_file_path = config["book_file_path"]

        update_index = Library.search_book("isbn", isbn, should_return = True)
        update_index = [index+1 for index in update_index]
        if len(update_index)>0:
            print("\nThis book will be updated. Do you wish to continue?")
            choice = input("Enter Y/N: ")
            if choice == "Y":
                updated_title = input("Enter new title: ")
                updated_author = input("Enter new author: ")
                updated_copies = input("Enter new number of copies: ")
                book = Book(updated_title, updated_author, isbn, updated_copies)
                storage.update(update_index, book, book_file_path)
                print("Updated successfully.")
            elif choice == "N":
                print ("Updation task aborted")
            else:
                print("Invalid choice, please try again.")
        else:
            print("Book not found. Updation task aborted.")

    @staticmethod
    def add_user(user):
        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        user_file_path = config["user_file_path"]
        storage.store(user, user_file_path)

    @staticmethod
    def list_all_users():
        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        user_file_path = config["user_file_path"]

        users_dict = storage.retrieve(user_file_path)

        if users_dict:
            keys = list(users_dict.keys())
            length = len(users_dict[keys[0]])
            users_list = [
                [users_dict[key][index] for key in keys] for index in range(length)
            ]
            for user in users_list:
                print(
                    "\nName: {}, User ID: {}".format(
                        user[0], user[1]
                    )
                )
        else:
            print("\nNo user registered in library")

    @staticmethod
    def search_user(search_field, search_query, should_return = False):
        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        user_file_path = config["user_file_path"]

        users_dict = storage.retrieve(user_file_path)
        indices = []
        if users_dict:
            for index, value in enumerate(users_dict[search_field]):
                if search_query == value:
                    indices.append(index)
            if len(indices) == 0:
                print("\nSearch result is empty. Search term not found.")
            else:
                print("\nThe search result(s) are:")
                for index in indices:
                    print(
                        "\nName: {}, User ID: {}".format(
                            users_dict["name"][index],
                            users_dict["userId"][index]
                        )
                    )
        else:
            print("\nNo user registered in library")
        if should_return == True:
            return (indices)

        
    @staticmethod
    def delete_user(search_field, search_query):

        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        user_file_path = config["user_file_path"]
    
        delete_indices = Library.search_user(search_field, search_query, should_return = True)
        delete_indices = [index+1 for index in delete_indices]
        if len(delete_indices)>0:
            print("\nThese users will be deleted. Do you wish to continue?")
            choice = input("Enter Y/N: ")
            if choice == "Y":
                storage.delete(delete_indices, user_file_path)
                print("\nDeleted successfully.")
            elif choice == "N":
                print("\nDeletion task aborted")
            else:
                print("\nInvalid choice, please try again.")
        else:
            print("\nUser not found. Deletion task aborted.")
    
    
    @staticmethod
    def update_user(user_id):

        configuration_file_location = get_configuration_file_location()
        config = get_configuration_file(configuration_file_location)
        user_file_path = config["user_file_path"]

        update_index = Library.search_user("userId", user_id, should_return = True)
        update_index = [index+1 for index in update_index]
        if len(update_index)>0:
            print("\nThis user will be updated. Do you wish to continue?")
            choice = input("Enter Y/N: ")
            if choice == "Y":
                updated_name = input("Enter new name: ")
                user = User(updated_name, user_id)
                storage.update(update_index, user, user_file_path)
                print("Updated successfully.")
            elif choice == "N":
                print ("Updation task aborted")
            else:
                print("Invalid choice, please try again.")
        else:
            print("Book not found. Updation task aborted.")


    @staticmethod
    def checkin_book(user_id, isbn):
        book_indices, availability = Library.search_book("isbn", isbn, stock_check_checkin = True)
        user_indices = Library.search_user("userId", user_id, should_return = True)
        checkin_date = str(date.today())
        if len(user_indices)>0 and len(book_indices)>0:
            if availability == 'Y':
                user_index = user_indices[0]
                book_index = book_indices[0]
                storage.checkin_book(user_id, isbn, book_index, user_index, checkin_date)
                print("Book checked in (Borrowed) successfully.")
            else:
                print("Book is already issued.")
        elif len(user_indices) == 0:
            print("User not registered.")
        elif len(book_indices) == 0:
            print("Book is not available in library.")


    @staticmethod
    def checkout_book(user_id, isbn):
        book_indices, issued_earlier = Library.search_book("isbn", isbn, stock_check_checkout = True)
        user_indices = Library.search_user("userId", user_id, should_return = True)
        checkout_date = str(date.today())
        if len(user_indices)>0 and len(book_indices)>0:
            if issued_earlier == 'Y':
                user_index = user_indices[0]
                book_index = book_indices[0]
                return_message = storage.checkout_book(user_id, isbn, book_index, user_index, checkout_date)
                print(return_message)
            else:
                print("Book had not been issued earlier.")
        elif len(user_indices) == 0:
            print("User not registered.")
        elif len(book_indices) == 0:
            print("Book is not available in library.")


            

            
            


