"""
FileName: User.py Author: Kunal Kundu Date: Feb 10,2024

File Description: Defines the User class for the Library Management System.
Represents library users with functionalities to manage their attributes and
issued books.

Design Comments: The class encapsulates user attributes in a dictionary for
flexible attribute management. Supports easy expansion to include additional
user-related details without modifying the class structure.
"""


class User():
    """
    Represents a library user, including their name, ID, and issued books.

    @Summary: Initializes a new User instance with name, user ID, and a list of
    issued books. @param name (str): The name of the user. @param user_id (str):
    The unique identifier for the user. @param issued (list): A list of books
    (represented by some form of identifier) issued to the user.
    """
    def __init__(self, name=None, user_id=None, issued=[]):
        self.attributes = {"name": name, "userId": user_id, "issued": issued}