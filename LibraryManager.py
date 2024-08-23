import os
import sqlite3
import Book

path = 'C:/Users/olitt/OneDrive/Documentos/python/LibraryManager/books.db'
isExisting = os.path.exist(path)


def display():
    print("1. Add books")
    print("2. Delete book")
    print("3. Search book")
    print("4. Quit")
    
def add_books():
    book_title = input("Enter title: ")
    book_author = input("Enter author: ")
    book_section = input("Enter section: ")
    book_isbn = input("Enter ISBN#: ")

    new_book = Book(book_title, book_author, book_section, book_isbn)

    new_book.add_book()


if not isExisting:
    # Connect to the database and create it if it doesn't exist
    conn = sqlite3.connect(path)
    c = conn.cursor()
    # Create the books table
    c.execute("""
        CREATE TABLE books (
            title TEXT,
            author TEXT,
            genre TEXT,
            isbn INTEGER
        )
    """)
    print("Database created and table 'books' initialized.")
else:
    # Connect to the existing database
    conn = sqlite3.connect(path)
    print("Connected to the existing database.")



while True:
    display()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("You chose to add books.")
        # Add books logic here
    elif choice == '2':
        print("You chose to delete a book.")
        # Delete book logic here
    elif choice == '3':
        print("You chose to search for a book.")
        # Search book logic here
    elif choice == '4':
        print("Quitting the program.")
        conn.close()
        break
    else:
        print("Invalid choice. Please choose again.")


