import storage

class Library():

    @staticmethod
    def add_book(book):
        storage.store(book)

    @staticmethod
    def list_all_books():

        books_dict = storage.retrieve()

        if books_dict:
            keys = list(books_dict.keys())
            length = len(books_dict[keys[0]])
            books_list = [[books_dict[key][index] for key in keys] for index in range(length)]
            for book in books_list:
                print("Title: {}, Author: {}, ISBN: {}".format(book[0],book[1],book[2]))
        else:
            print("No books stored")

    @staticmethod
    def search_books():
        


