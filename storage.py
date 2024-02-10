import csv
import os

def store(book):

    file_path = "books.csv"

    if os.path.exists(file_path):
        with open(file_path, mode = 'a') as file:
            fieldnames = book.attributes.keys()
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writerow(book.attributes)

    else:
        with open(file_path, mode = 'w') as file:
            fieldnames = book.attributes.keys()
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow(book.attributes)


def retrieve():
    
    file_path = "books.csv"

    books_dict={"title":[],"author":[],"isbn":[]}

    if os.path.exists(file_path):
        with open(file_path, mode = 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                books_dict["title"].append(row[0])
                books_dict["author"].append(row[1])
                books_dict["isbn"].append(row[2])
            return (books_dict)
    else:
        print("No books stored")
        return



