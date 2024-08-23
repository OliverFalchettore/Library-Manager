import db # Import the database connection and cursor from db.py


class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre # type: ignore
        self.isbn = isbn


    #TODO: Add books to the database
    def add_book(self):
        db.c.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
                                 (self.title, self.author, self.genre, self.isbn)
                                )
        db.conn.commit()

    #TODO: Delete books from the database    
    def delete_book(self, rowid):
        pass

