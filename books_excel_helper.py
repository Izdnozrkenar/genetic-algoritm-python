import csv
from book import Book

def get_books_csv_data(): 
    with open('books_data.csv',mode='r') as books_codes:
        data = csv.reader(books_codes)

        books = []

        for row in data:
            books.append(Book(row[0]))

        return books