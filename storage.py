import csv
import os
from utils import get_configuration_file_location, get_configuration_file
import pandas as pd
from ast import literal_eval


def store(object, file_path):

    if os.path.exists(file_path):
        with open(file_path, mode='a') as file:
            fieldnames = object.attributes.keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(object.attributes)

    else:
        with open(file_path, mode='w') as file:
            fieldnames = object.attributes.keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(object.attributes)


def retrieve(file_path):

    object_dict = {}

    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for key in reader.fieldnames:
                object_dict[key] = []
            for row in reader:
                for key in row.keys():
                    object_dict[key].append(row[key])
            return (object_dict)
    else:
        print("No value is stored. Storage is empty.")
        return


def delete(indices, file_path):

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        rows = [row for index, row in enumerate(rows) if index not in indices]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def update(indices, object, file_path):

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for i, key in enumerate(object.attributes):
            if key == "copies":
                rows[indices[0]][i] = rows[indices[0]][i] + object.attributes[key]
            else:
                rows[indices[0]][i] = object.attributes[key]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def checkin_book(user_id, isbn, book_index, user_index, checkin_date, checkout_date=None):
    configuration_file_location = get_configuration_file_location()
    config = get_configuration_file(configuration_file_location)
    book_file_path = config["book_file_path"]
    user_file_path = config["user_file_path"]

    books_data = pd.read_csv(book_file_path, converters={"issuedTo": literal_eval})
    books_data.loc[book_index, 'borrowed'] = books_data.loc[book_index, 'borrowed']+1
    books_data.loc[book_index, 'issuedTo'].append(user_id)
    books_data.to_csv(book_file_path, index=False)

    users_data = pd.read_csv(user_file_path, converters={"issued": literal_eval})
    users_data.loc[user_index, "issued"].append([isbn,checkin_date,checkout_date])
    users_data.to_csv(user_file_path, index=False)


def checkout_book(user_id, isbn, book_index, user_index, checkout_date):
    configuration_file_location = get_configuration_file_location()
    config = get_configuration_file(configuration_file_location)
    book_file_path = config["book_file_path"]
    user_file_path = config["user_file_path"]

    books_data = pd.read_csv(book_file_path, converters={"issuedTo": literal_eval})
    books_data.loc[book_index, 'borrowed'] = books_data.loc[book_index, 'borrowed']-1
    books_data.loc[book_index, 'issuedTo'].remove(user_id)
    books_data.to_csv(book_file_path, index=False)

    users_data = pd.read_csv(user_file_path, converters={"issued": literal_eval})
    message = "The book had not been issued by this user."
    for index, book in enumerate(users_data.loc[user_index, "issued"]):
        if book[0] == isbn and book[2] == None:
            users_data.loc[user_index, "issued"][index][2] = checkout_date
            message = "Book checked out (Returned) successfully."
            break
    users_data.to_csv(user_file_path, index=False)
    return (message)
