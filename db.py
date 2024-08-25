import sqlite3
import os 

path = 'C:/Users/olitt/Documents/python/Library-Manager/books.db'
isExisting = os.path.exists(path)

conn = sqlite3.connect(path)
c = conn.cursor()


def initialize_database():
    if not isExisting:
        # Create the books table
        c.execute("""
            CREATE TABLE books (
                title TEXT,
                author TEXT,
                genre TEXT,
                isbn TEXT
            )
        """)
        conn.commit()
        print("Database created and table 'books' initialized.")
    else:
        # Connect to the existing database
        conn = sqlite3.connect(path)
        print("Connected to the existing database.")

initialize_database()