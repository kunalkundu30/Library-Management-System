"""
FileName: storage.py
Author: Kunal Kundu
Date: Feb 10,2024

File Description:
- Handles data storage operations for the Library Management System.
- Provides functionality to store, retrieve, delete and update records in CSV format.
- Supports check-in and check-out processes for books with user tracking.

Design Comments:
- Uses CSV files for data persistence, enabling straightforward integration and manual editing.
- Incorporates pandas for complex data manipulations, enhancing efficiency and capability in handling book and user records.
- Leverages Python's standard library for file handling, ensuring compatibility and simplicity.
"""


import csv
import os
from utils import get_configuration_file_location, get_configuration_file
import pandas as pd
from ast import literal_eval
import sys
import logging


def store(object, file_path):
    """
    @Summary: Stores an object's attributes in a CSV file.
    @param object (Object): The object with attributes to store.
    @param file_path (str): Path to the CSV file.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, mode='a') as file:
                fieldnames = object.attributes.keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(object.attributes)
        except FileNotFoundError as e:
            print("Error opening file {}.  The Exception is: {}".format(file_path, e))
            logging.error("Error opening file {}.  The Exception is: {}".format(file_path, e))
            sys.exit(1)

    else:
        try:
            with open(file_path, mode='w') as file:
                fieldnames = object.attributes.keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(object.attributes)
        except FileNotFoundError as e:
            print("Error opening file {}.  The Exception is: {}".format(file_path, e))
            logging.error("Error opening file {}.  The Exception is: {}".format(file_path, e))
            sys.exit(1)


def retrieve(file_path):
    """
    @Summary: Retrieves and returns data from a CSV file as a dictionary.
    @param file_path (str): Path to the CSV file.
    @return (dict): Dictionary containing the data, or None if file doesn't exist.
    """
    object_dict = {}

    if os.path.exists(file_path):
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for key in reader.fieldnames:
                    object_dict[key] = []
                for row in reader:
                    for key in row.keys():
                        object_dict[key].append(row[key])
                return (object_dict)
        except FileNotFoundError as e:
            print("Error opening file {}.  The Exception is: {}".format(file_path, e))
            logging.error("Error opening file {}.  The Exception is: {}".format(file_path, e))
            sys.exit(1)
    else:
        print("Storage is empty.")
        return


def delete(indices, file_path):
    """
    @Summary: Deletes rows from a CSV file based on provided indices.
    @param indices (list): List of row indices to delete.
    @param file_path (str): Path to the CSV file.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            rows = [row for index, row in enumerate(rows) if index not in indices]

    except FileNotFoundError as e:
        print("Error opening file {}.  The Exception is: {}".format(file_path, e))
        logging.error("Error opening file {}.  The Exception is: {}".format(file_path, e))
        sys.exit(1)

    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    except FileNotFoundError as e:
        print("Error opening file {}.  The Exception is: {}".format(file_path, e))
        logging.error("Error opening file {}.  The Exception is: {}".format(file_path, e))
        sys.exit(1)


def update(indices, object, file_path):
    """
    @Summary: Updates specific rows in a CSV file based on provided indices.
    @param indices (list): List of row indices to update.
    @param object (Object): The object with updated attributes.
    @param file_path (str): Path to the CSV file.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            for i, key in enumerate(object.attributes):
                if key == "copies":
                    rows[indices[0]][i] = rows[indices[0]][i] + object.attributes[key]
                else:
                    rows[indices[0]][i] = object.attributes[key]

    except FileNotFoundError as e:
        print("Error opening file {}.  The Exception is: {}".format(file_path, e))
        logging.error("Error opening file {}.  The Exception is: {}".format(file_path, e))
        sys.exit(1)

    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except FileNotFoundError as e:
        print("Error opening file {}.  The Exception is: {}".format(file_path, e))
        logging.error("Error opening file {}.  The Exception is: {}".format(file_path, e))
        sys.exit(1)


def checkin_book(user_id, isbn, book_index, user_index, checkin_date, checkout_date=None):
    """
    @Summary: Records a book check-in by updating book and user data.
    @param user_id (str): ID of the user checking in the book.
    @param isbn (str): ISBN of the book.
    @param book_index (int): Index of the book in the CSV file.
    @param user_index (int): Index of the user in the CSV file.
    @param checkin_date (str): Date of book check-in.
    @param checkout_date (str, optional): Date of book check-out, if applicable.
    """
    configuration_file_location = get_configuration_file_location()
    config = get_configuration_file(configuration_file_location)
    book_file_path = config["book_file_path"]
    user_file_path = config["user_file_path"]

    try:
        books_data = pd.read_csv(book_file_path, converters={"issuedTo": literal_eval})
    except FileNotFoundError as e:
        print("Error opening file {}.  The Exception is: {}".format(book_file_path, e))
        logging.error("Error opening file {}.  The Exception is: {}".format(book_file_path, e))
        sys.exit(1)

    books_data.loc[book_index, 'borrowed'] = books_data.loc[book_index, 'borrowed']+1
    books_data.loc[book_index, 'issuedTo'].append(user_id)
    books_data.to_csv(book_file_path, index=False)

    try:
        users_data = pd.read_csv(user_file_path, converters={"issued": literal_eval})
    except FileNotFoundError as e:
        print("Error opening file {}.  The Exception is: {}".format(user_file_path, e))
        logging.error("Error opening file {}.  The Exception is: {}".format(user_file_path, e))
        sys.exit(1)

    users_data.loc[user_index, "issued"].append([isbn,checkin_date,checkout_date])
    users_data.to_csv(user_file_path, index=False)


def checkout_book(user_id, isbn, book_index, user_index, checkout_date):
    """
    @Summary: Processes a book checkout by updating the corresponding book and user data.
    @param user_id (str): ID of the user checking out the book.
    @param isbn (str): ISBN of the book.
    @param book_index (int): Index of the book in the CSV file.
    @param user_index (int): Index of the user in the CSV file.
    @param checkout_date (str): Date of book check-out.
    @return (str): Message indicating the outcome of the checkout process.
    """
    configuration_file_location = get_configuration_file_location()
    config = get_configuration_file(configuration_file_location)
    book_file_path = config["book_file_path"]
    user_file_path = config["user_file_path"]

    try:
        books_data = pd.read_csv(book_file_path, converters={"issuedTo": literal_eval})
    except FileNotFoundError as e:
        print("Error opening file {}.  The Exception is: {}".format(book_file_path, e))
        logging.error("Error opening file {}.  The Exception is: {}".format(book_file_path, e))
        sys.exit(1)

    books_data.loc[book_index, 'borrowed'] = books_data.loc[book_index, 'borrowed']-1
    books_data.loc[book_index, 'issuedTo'].remove(user_id)
    books_data.to_csv(book_file_path, index=False)

    try:
        users_data = pd.read_csv(user_file_path, converters={"issued": literal_eval})
    except FileNotFoundError as e:
        print("Error opening file {}.  The Exception is: {}".format(user_file_path, e))
        logging.error("Error opening file {}.  The Exception is: {}".format(user_file_path, e))
        sys.exit(1)

    message = "The book had not been issued by this user."
    for index, book in enumerate(users_data.loc[user_index, "issued"]):
        if book[0] == isbn and book[2] == None:
            users_data.loc[user_index, "issued"][index][2] = checkout_date
            message = "Book checked out (Returned) successfully."
            break
    users_data.to_csv(user_file_path, index=False)
    return (message)
