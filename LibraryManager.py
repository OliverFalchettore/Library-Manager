import sqlite3
import Book
from os.path import exists

path = 'C:/Users/olitt/OneDrive/Documentos/python/LibraryManager/books.db'
isExisting = os.path.exist(path)

def display():
    print("1. Add books")
    print("2. Delete book")
    print("3. Search book")
    
def add_books():
    book_title = input("Enter title: ")
    book_author = input("Enter author: ")
    book_section = input("Enter section: ")
    book_isbn = input("Enter ISBN#: ")

    new_book = Book(book_title, book_author, book_section, book_isbn)

    new_book.add_book()


if not isExisting:
    conn = sqlite3.connect('books.db')
    c.execute("""CREATE TABLE books (
              title TEXT,
              author TEXT
              genre TEXT,
              isbn INTEGER,
    )""")
else:
    conn = sqlite3.connect('books.db')

c = conn.cursor()

user_input = input(">>>")




