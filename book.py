"""
FileName: Book.py
Author: Kunal Kundu
Date: Feb 10,2024

File Description: Defines the Book class, representing books within the Library Management System.
This class encapsulates book attributes such as title, author, ISBN, available copies, borrowed count, and list of users it is issued to.

Design Comments: The Book class uses a dictionary to store its attributes, offering a flexible and dynamic way to handle book properties.
This approach simplifies attribute management, supports easy modifications for future enhancements, and facilitates serialization for data storage and retrieval.
"""


class Book:
    """
    Represents a book with comprehensive details, suitable for library management.

    @Summary: Initializes a new instance of the Book class with detailed attributes.
    @param title (str): The title of the book.
    @param author (str): The author of the book.
    @param isbn (str): The International Standard Book Number for the book.
    @param copies (int): The total number of copies of the book available.
    @param borrowed (int): The count of copies currently borrowed.
    @param issued_to (list): The list of user IDs to whom copies of the book are issued.
    """
    def __init__(self, title=None, author=None, isbn=None, copies = 0, borrowed = 0, issued_to=[]):
        self.attributes = {"title": title, "author": author, "isbn": isbn, "copies": copies, "borrowed": borrowed, "issuedTo":issued_to}