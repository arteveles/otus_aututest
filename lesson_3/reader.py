import csv
import json


result = []


class ReadData:


    @property
    def read_json_users(self):
        with open("data/users.json", "r") as file:
            extracted_users = json.load(file)
            for user in extracted_users:
                result.append({
                    'name': user['name'],
                    'gender': user['gender'],
                    'address': user['address'],
                    'age': user['age'],
                    'books': []
                })

    @property
    def read_csv_books(self):
        with open("data/books.csv", "r") as file:
            extracted_books = csv.DictReader(file)
            i = 0
            for book in extracted_books:
                result[i % len(result)]['extracted_books'].append({
                    'title': book['Title'],
                    'author': book['Author'],
                    'pages': book['Pages'],
                    'genre': book['Genre']
                })
                i += 1


print(result)
