# Python_miniproject_Library_Management

1.	Create a class Book with the following attributes:
	•	book_id (unique ID for each book)
	•	title (book title)
	•	author (author name)
	•	available (boolean → True if available, False if borrowed)
Include a _str_() method to display book details in a readable format.
	2.	Create a class Library with the following methods:
	•	add_book(book) → Add a new book to the library.
	•	display_books() → Display all books with their status (Available/Not Available).
	•	borrow_book(book_id) → Borrow a book if it is available.
	•	return_book(book_id) → Return a borrowed book.
	3.	Implement a menu-driven program that allows the user to:
	•	Add a new book
	•	Display all books
	•	Borrow a book by entering its ID
	•	Return a book by entering its ID
	•	Exit the program
