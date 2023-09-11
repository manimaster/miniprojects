# Define data structures for books and users
class Book:
    def __init__(self, id, title, author, price, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.cart = []

# Global variables to store books and users
books = [
    Book(1, "Book 1", "Author 1", 19.99, 5),
    Book(2, "Book 2", "Author 2", 14.99, 3),
    Book(3, "Book 3", "Author 3", 9.99, 7)
]

users = []
current_user = None

# Function to display a list of books
def display_books():
    print("Available Books:")
    print("-----------------------------")
    for book in books:
        print(f"ID: {book.id}")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Price: ${book.price}")
        print(f"Quantity: {book.quantity}")
        print("-----------------------------")

# Function to handle user registration
def register_user():
    global users
    user_id = len(users) + 1
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    user = User(user_id, username, password)
    users.append(user)
    print("Registration successful. Please log in.")

# Function to handle user login
def login_user():
    global current_user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in users:
        if user.username == username and user.password == password:
            current_user = user
            print(f"Login successful. Welcome, {user.username}!")
            return
    print("Invalid username or password. Please try again.")

# Function to add a book to the user's cart
def add_to_cart(book_id):
    global current_user
    if current_user is None:
        print("Please log in to add items to your cart.")
        return
    for book in books:
        if book.id == book_id:
            if book.quantity > 0:
                current_user.cart.append(book)
                book.quantity -= 1
                print(f"Added to cart: {book.title}")
                return
            else:
                print("Sorry, this book is out of stock.")
                return
    print("Invalid book ID. Please try again.")

# Function to display the user's cart
def display_cart():
    global current_user
    if current_user is None:
        print("Please log in to view your cart.")
        return
    print("Your Cart:")
    print("-----------------------------")
    for book in current_user.cart:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Price: ${book.price}")
        print("-----------------------------")

while True:
    print("Online Bookstore Management System")
    print("1. Register")
    print("2. Login")
    print("3. List Books")
    print("4. Add to Cart")
    print("5. View Cart")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        display_books()
    elif choice == '4':
        book_id = int(input("Enter the ID of the book you want to add to your cart: "))
        add_to_cart(book_id)
    elif choice == '5':
        display_cart()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
