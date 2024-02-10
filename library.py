import storage


class Library:

    @staticmethod
    def add_book(book):
        storage.store(book)

    @staticmethod
    def list_all_books():

        books_dict = storage.retrieve()

        if books_dict:
            keys = list(books_dict.keys())
            length = len(books_dict[keys[0]])
            books_list = [
                [books_dict[key][index] for key in keys] for index in range(length)
            ]
            for book in books_list:
                print(
                    "Title: {}, Author: {}, ISBN: {}".format(
                        book[0], book[1], book[2]
                    )
                )
        else:
            print("No books in library")

    @staticmethod
    def search_book(search_field, search_query):

        books_dict = storage.retrieve()
        indices = []
        if books_dict:
            for index, value in enumerate(books_dict[search_field]):
                if search_query == value:
                    indices.append(index)
            if len(indices) == 0:
                print ("Search result is empty. Search term not found.")
            else:
                print("\nThe search result(s) are:")
                for index in indices:
                    print(
                        "Title: {}, Author: {}, ISBN: {}".format(
                            books_dict["title"][index],
                            books_dict["author"][index],
                            books_dict["isbn"][index],
                        )
                    )
        else:
            print("No books in library")
