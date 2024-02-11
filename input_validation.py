"""
FileName: input_validation.py
Author: Kunal Kundu
Date: Feb 10,2024

File Description:
- Handles validation of inputs given by user for the Library Management System.
- Provides functionality to raise errors until the user puts the correct response.

Design Comments:
- Centralises input validation for consistency.
- Uses different methods for each input for easy editing/customisation in future.
- Repeatedly raises errors to guide user to input the correct data.
- Ensures correct, clean and expected data is used in the application.
"""


def input_title(message):
    """
    @Summary: Takes input of title of book from user.
    @param message (str): Message to be dispalyed while taking input.
    @return (str): Title of the book
    """
    while True:
        try:
            user_input = input(message)
            if len(user_input)>200 or not user_input.strip():
                raise ValueError("Title is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")
    

def input_author(message):
    """
    @Summary: Takes input of author of book from user.
    @param message (str): Message to be dispalyed while taking input.
    @return (str): Author of the book
    """
    while True:
        try:
            user_input = input(message)
            if len(user_input)>200 or not user_input.strip() or not user_input.isalnum():
                raise ValueError("Author is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")


def input_isbn(message):
    """
    @Summary: Takes input of ISBN of book from user.
    @param message (str): Message to be dispalyed while taking input.
    @return (str): ISBN of the book
    """
    while True:
        try:
            user_input = input(message)
            if len(user_input)>20 or not user_input.strip() or not user_input.isdigit():
                raise ValueError("ISBN is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")

            
def input_quantity(message):
    """
    @Summary: Takes input of quantity of book from user.
    @param message (str): Message to be dispalyed while taking input.
    @return (int): Quantity of the book
    """
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("The input is not integer, please try again")
        else:
            return user_input
        

def input_user_name(message):
    """
    @Summary: Takes input of name of the user.
    @param message (str): Message to be dispalyed while taking input.
    @return (str): User name.
    """
    while True:
        try:
            user_input = input(message)
            if len(user_input)>200 or not user_input.strip() or not user_input.isalnum():
                raise ValueError("User Name is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")

            
def input_user_id(message):
    """
    @Summary: Takes input of id of user.
    @param message (str): Message to be dispalyed while taking input.
    @return (str): User ID.
    """
    while True:
        try:
            user_input = input(message)
            if len(user_input)>20 or not user_input.strip() or not user_input.isalnum():
                raise ValueError("User ID is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")