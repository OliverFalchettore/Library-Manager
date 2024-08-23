import os
from Book import Book
import db


def display():
    print("1. Add books")
    print("2. Delete book")
    print("3. Display all books")
    print("4. Quit")
    
def add_books():
    book_title = input("Enter title: ")
    book_author = input("Enter author: ")
    book_genre = input("Enter genre: ")
    book_isbn = input("Enter ISBN#: ")

    new_book = Book(book_title, book_author, book_genre, book_isbn)

    new_book.add_book()

#Make it display all the books in database
def search_book():
    db.c.execute("SELECT * FROM books")
    items = db.c.fetchall()

    # Print table headers
    print(f"{'TITLE':<30}{'AUTHOR':<25}{'GENRE':<20}{'ISBN#':<15}")
    print(f"{'-'*30}{'-'*25}{'-'*20}{'-'*15}")

    # Print each item in a formatted way
    for item in items:
        title, author, genre, isbn = item
        print(f"{title:<30}{author:<25}{genre:<20}{isbn:<15}")

while True:
    display()
    choice = input("Enter your choice: ")  
    if choice == '1':
        add_books()
    elif choice == '2':
        print("You chose to delete a book.")
        # Delete book logic here
    elif choice == '3':
        search_book()
    elif choice == '4':
        print("Quitting the program.")
        db.conn.close()
        break
    else:
        print("Invalid choice. Please choose again.")


