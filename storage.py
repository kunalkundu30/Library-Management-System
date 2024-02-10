import csv
import os


def store(book):

    file_path = "books.csv"

    if os.path.exists(file_path):
        with open(file_path, mode='a') as file:
            fieldnames = book.attributes.keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(book.attributes)

    else:
        with open(file_path, mode='w') as file:
            fieldnames = book.attributes.keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(book.attributes)


def retrieve():

    file_path = "books.csv"

    books_dict = {}

    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for key in reader.fieldnames:
                books_dict[key] = []
            for row in reader:
                for key in row.keys():
                    books_dict[key].append(row[key])
            return (books_dict)
    else:
        print("No books stored")
        return


def delete(indices):

    file_path = "books.csv"

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        rows = [row for index, row in enumerate(rows) if index not in indices]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)



