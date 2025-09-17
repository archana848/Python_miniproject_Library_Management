class Book():
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"ID: {self.book_id} Title: {self.title} Author: {self.author} Status: {status}"

class Library():
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        self.books.append(Book(book_id, title, author))
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self):
        book_id = input("Enter Book ID to borrow: ")
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print(f"You borrowed: {book.title}")
                else:
                    print("Book is already borrowed.")
                return
        print("Book ID not found.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print(f"You returned: {book.title}")
                else:
                    print("Book was not borrowed.")
                return
        print("Book ID not found.")


def library_menu(lib):
    print("\nLibrary Management System")
    print("1. Add Book\n2. Display Books\n3. Borrow Book\n4. Return Book\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        lib.add_book()
    elif choice == "2":
        lib.display_books()
    elif choice == "3":
        lib.borrow_book()
    elif choice == "4":
        lib.return_book()
    elif choice == "5":
        print("Exiting Library System.")
        return 
    else:
        print("Invalid choice.")

    library_menu(lib)

ob = Library()
library_menu(ob)