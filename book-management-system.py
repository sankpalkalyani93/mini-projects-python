# library management system
#1. Initializing the library catalog containing book information 

library_catlog = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
]

#2. Tracking borrowed books - we can use a dictionary with user id 
# and key and borrowed book id as values
borrowed_books = {}

#3. to track available book id s we can use set which will help in maintaining unique book ids
available_books = set(book["id"] for book in library_catlog)

#4 functionalities : 
#4.1 View the library catlog
def view_library_catlog():
    print("Library Catlog")
    for book in library_catlog:
        print(f"{book["id"]} : {book["title"]} : {book["author"]}")

#4.2 adding book to library catlog
def add_book_to_library_catlog(book_id, book_title, book_author):
    library_catlog.append({"id": book_id, "title": book_title, "author": book_author})
    view_library_catlog()

#4.3 borrow book 
def borrow_book(user_id, book_id):
    if book_id in available_books:
        if user_id not in borrowed_books:
            borrowed_books[user_id] = set()
        borrowed_books[user_id].add(book_id)
        print(f"Book ID {book_id} borrowed by User with {user_id}.")
    else:
        print("The book is currently unavailable.")

#4.return book
def return_book(user_id, book_id):
    if user_id in borrowed_books and book_id in borrowed_books[user_id]:
        borrowed_books[user_id].remove(book_id)
        print(f"Book ID {book_id} returned by user ID {user_id}.")
    else:
        print("This book was not borrowed by this user.")

view_library_catlog()
add_book_to_library_catlog(4, "The Adventures of Tom Sawyer", "Mark Twain")
borrow_book(1100, 7)
borrow_book(1100, 2)
return_book(1100, 2)