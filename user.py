"""
FileName: User.py
Author: Kunal Kundu
Date: Feb 10,2024

File Description:
Defines the User class for the Library Management System.
Represents library users with functionalities to manage their attributes and issued books.

Design Comments:
The class encapsulates user attributes in a dictionary for flexible attribute management.
Supports easy expansion to include additional user-related details without modifying the class structure.
"""


class User():

    def __init__(self, name=None, user_id=None, issued=[]):
        self.attributes = {"name": name, "userId": user_id, "issued": issued}