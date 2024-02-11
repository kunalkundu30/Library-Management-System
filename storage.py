import csv
import os


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
            rows[indices[0]][i] = object.attributes[key]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)



