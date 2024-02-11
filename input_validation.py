"""
FileName: input_validation.py
Author: Kunal Kundu
Date: Feb 10,2024

File Description:
- Handles validation of inputs given by user for the Library Management System.
- Provides functionality to raise errors until the user puts the correct response.

Design Comments:
- Uses different methods for each input for easy editing/customisation in future.
- Repeatedly raises errors to guide user to input the correct data.
- Ensures correct, clean and expected data is used in the application.
"""


def input_title():
    """
    @Summary: Takes input of title of book from user.
    @return (str): Title of the book
    """
    while True:
        try:
            user_input = input("Enter title: ")
            if len(user_input)>200 or not user_input.strip():
                raise ValueError("Title is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")
    

def input_author():
    """
    @Summary: Takes input of author of book from user.
    @return (str): Author of the book
    """
    while True:
        try:
            user_input = input("Enter author: ")
            if len(user_input)>200 or not user_input.strip() or not user_input.isalnum():
                raise ValueError("Author is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")


def input_isbn():
    """
    @Summary: Takes input of ISBN of book from user.
    @return (str): ISBN of the book
    """
    while True:
        try:
            user_input = input("Enter ISBN: ")
            if len(user_input)>20 or not user_input.strip() or not user_input.isdigit():
                raise ValueError("ISBN is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")

            
def input_quantity():
    """
    @Summary: Takes input of quantity of book from user.
    @return (int): Quantity of the book
    """
    while True:
        try:
            user_input = int(input("Enter Quantity: "))
        except ValueError:
            print("The input is not integer, please try again")
        else:
            return user_input
        

def input_user_name():
    """
    @Summary: Takes input of name of the user.
    @return (str): User name.
    """
    while True:
        try:
            user_input = input("Enter user name: ")
            if len(user_input)>200 or not user_input.strip() or not user_input.isalnum():
                raise ValueError("User Name is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")

            
def input_user_id():
    """
    @Summary: Takes input of id of user.
    @return (str): User ID.
    """
    while True:
        try:
            user_input = input("Enter user id: ")
            if len(user_input)>20 or not user_input.strip() or not user_input.isalnum():
                raise ValueError("User ID is incorrect, please try again.")
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")