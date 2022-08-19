import csv
import json

result = []


def read_json_users():
    with open("data/users.json", "r") as file:
        extracted_users = json.load(file)
        for user in extracted_users:
            result.append(
                {
                    'name': user['name'],
                    'gender': user['gender'],
                    'address': user['address'],
                    'age': user['age'],
                    'books': []
                }
            )


def read_csv_books():
    with open("data/books.csv", "r") as file:
        books = csv.DictReader(file)
        i = 0
        for book in books:
            result[i % len(result)]['books'].append({
                'title': book['Title'],
                'author': book['Author'],
                'pages': book['Pages'],
                'genre': book['Genre']
            })
            i += 1
