# Global list to store books
import storage

class Book:

    def __init__(self, title=None, author=None, isbn=None):
        self.attributes = {'title':title,'author':author,'isbn':isbn}


    

    def add(self):
        storage.store(self)

    @staticmethod
    def list_books():

        books_data = storage.retrieve()
        if books_data:
            
        else:
            print("No books stored")

    # def search(self):
        
        





# books = []

# def add_book(title, author, isbn):
#     books.append({"title": title, "author": author, "isbn": isbn})

# def list_books():
#     for book in books:
#         print(book)

