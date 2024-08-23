import os
from Book import Book
import db


def display():
    print("1. Add books")
    print("2. Delete book")
    print("3. Search book")
    print("4. Quit")
    
def add_books():
    book_title = input("Enter title: ")
    book_author = input("Enter author: ")
    book_genre = input("Enter genre: ")
    book_isbn = input("Enter ISBN#: ")

    new_book = Book(book_title, book_author, book_genre, book_isbn)

    new_book.add_book()


while True:
    display()
    choice = input("Enter your choice: ")  
    if choice == '1':
        add_books()
    elif choice == '2':
        print("You chose to delete a book.")
        # Delete book logic here
    elif choice == '3':
        print("You chose to search for a book.")
        # Search book logic here
    elif choice == '4':
        print("Quitting the program.")
        db.conn.close()
        break
    else:
        print("Invalid choice. Please choose again.")


