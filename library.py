import storage
from book import Book
from user import User
from utils import get_configuration_file_location, get_configuration_file


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
    def search_book(search_field, search_query, should_return = False):
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
                updated_author = input("Enter author: ")
                updated_isbn = input("Enter ISBN: ")
                book = Book(updated_title, updated_author, updated_isbn)
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
                updated_user_id = input("Enter new user ID: ")
                user = User(updated_name, updated_user_id)
                storage.update(update_index, user, user_file_path)
                print("Updated successfully.")
            elif choice == "N":
                print ("Updation task aborted")
            else:
                print("Invalid choice, please try again.")
        else:
            print("Book not found. Updation task aborted.")