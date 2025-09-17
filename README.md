# Python_miniproject_Library_Management

Design a simple Library Management System using Object-Oriented Programming (OOP) concepts in Python. The system should allow users to manage books in a library, including adding new books, displaying book details, borrowing books, and returning them. The program should be menu-driven to allow interaction through the command line.

1. Class: Book
Create a class named Book with the following attributes:
book_id: A unique identifier for each book.
title: The title of the book.
author: The name of the book’s author.
available: A boolean value (True if the book is available, False if borrowed).
Include a __str__() method to display book details in a readable format.
2. Class: Library
Create a class named Library that manages a collection of books and provides the following methods:
add_book(book): Adds a new book to the library collection.
display_books(): Displays all books with their availability status (Available / Not Available).
borrow_book(book_id): Allows a user to borrow a book by its ID if it is available.
return_book(book_id): Allows a user to return a borrowed book using its ID.
3. Menu-Driven Program
Implement a menu-based interface that repeatedly presents the user with options to:
Add a new book
Display all books
Borrow a book by entering its ID
Return a book by entering its ID
Exit the program
The program should perform input validation and provide appropriate feedback to the user for each operation.


output :-
Library Management System
1. Add Book
2. Display Books
3. Borrow Book
4. Return Book
5. Exit
Enter your choice (1-5): 1
Enter Book ID: 101
Enter Book Title: premalekhanam
Enter Author: basheer
Book added successfully.

Library Management System
1. Add Book
2. Display Books
3. Borrow Book
4. Return Book
5. Exit
Enter your choice (1-5): 1
Enter Book ID: 102
Enter Book Title: aadujeevitham
Enter Author: benyamin
Book added successfully.

Library Management System
1. Add Book
2. Display Books
3. Borrow Book
4. Return Book
5. Exit
Enter your choice (1-5): 2
ID: 101 Title: premalekhanam Author: basheer Status: Available
ID: 102 Title: aadujeevitham Author: benyamin Status: Available

Library Management System
1. Add Book
2. Display Books
3. Borrow Book
4. Return Book
5. Exit
Enter your choice (1-5): 3
Enter Book ID to borrow: 102
You borrowed: aadujeevitham

Library Management System
1. Add Book
2. Display Books
3. Borrow Book
4. Return Book
5. Exit
Enter your choice (1-5): 3
Enter Book ID to borrow: 203
Book ID not found.

Library Management System
1. Add Book
2. Display Books
3. Borrow Book
4. Return Book
5. Exit
Enter your choice (1-5): 4
Enter Book ID to return: 102
You returned: aadujeevitham

Library Management System
1. Add Book
2. Display Books
3. Borrow Book
4. Return Book
5. Exit
Enter your choice (1-5): 5
Exiting Library System.
