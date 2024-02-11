# Global list to store books


class Book:

    def __init__(self, title=None, author=None, isbn=None, copies = 0, borrowed = 0, issued_to=[]):
        self.attributes = {"title": title, "author": author, "isbn": isbn, "copies": copies, "borrowed": borrowed, "issuedTo":issued_to}


# books = []

# def add_book(title, author, isbn):
#     books.append({"title": title, "author": author, "isbn": isbn})

# def list_books():
#     for book in books:
#         print(book)
