# Name: <Your Name>
# Date: 27 Nov 2025
# Assignment 3 – Library Inventory System (All Tasks Combined)

import json

# ================================================================
#                           TASK 2
#                       BOOK CLASS
# ================================================================

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow(self):
        """Marks the book as not available"""
        self.available = False

    def return_book(self):
        """Marks the book as available"""
        self.available = True

    def to_dict(self):
        """Convert object to dictionary for JSON storage"""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        """Create Book object from JSON dict"""
        return cls(
            data["title"],
            data["author"],
            data["isbn"],
            data["available"]
        )


# ================================================================
#                           TASK 2
#                       MEMBER CLASS
# ================================================================

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book.isbn)
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book is not available")

    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.isbn)
            print(f"{self.name} returned {book.title}")
        else:
            print("This member never borrowed this book")

    def list_books(self):
        return self.borrowed_books

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        m = cls(data["name"], data["member_id"])
        m.borrowed_books = data["borrowed_books"]
        return m


# ================================================================
#                           TASK 3
#                      LIBRARY MANAGEMENT
# ================================================================

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()   # Loads saved data at startup (Task 4)

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()
        print("Book added successfully!")

    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
        self.save_data()
        print("Member registered successfully!")

    def lend_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if member and book:
            member.borrow_book(book)
            self.save_data()
        else:
            print("Invalid member ID or book ISBN")

    def take_return(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if member and book:
            member.return_book(book)
            self.save_data()
        else:
            print("Invalid return details")

    # ================================================================
    #                           TASK 4
    #                       FILE PERSISTENCE
    # ================================================================

    def save_data(self):
        try:
            with open("books.json", "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)

            with open("members.json", "w") as f:
                json.dump([m.to_dict() for m in self.members], f, indent=4)

        except Exception as e:
            print("Error saving data:", e)

    def load_data(self):
        try:
            with open("books.json", "r") as f:
                self.books = [Book.from_dict(d) for d in json.load(f)]
        except:
            self.books = []

        try:
            with open("members.json", "r") as f:
                self.members = [Member.from_dict(d) for d in json.load(f)]
        except:
            self.members = []

    # ================================================================
    #                           TASK 5
    #                      ANALYTICS / MINI REPORT
    # ================================================================

    def analytics(self):
        borrowed_count = sum(not b.available for b in self.books)
        total_members = len(self.members)

        print("\n---- Library Report ----")
        print(f"Total Members: {total_members}")
        print(f"Books currently borrowed: {borrowed_count}")
        print("------------------------\n")


# ================================================================
#                           TASK 1 + TASK 6
#                      MAIN MENU / USER INTERFACE
# ================================================================

def main():
    lib = Library()

    print("=====================================")
    print(" Welcome to the Python Library System ")
    print("=====================================\n")

    while True:
        print("\n1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Library Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            lib.add_book(title, author, isbn)

        elif choice == "2":
            name = input("Enter member name: ")
            mid = input("Enter member ID: ")
            lib.register_member(name, mid)

        elif choice == "3":
            mid = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            lib.lend_book(mid, isbn)

        elif choice == "4":
            mid = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            lib.take_return(mid, isbn)

        elif choice == "5":
            lib.analytics()

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, try again!")


# ================================================================
#                      EXECUTION ENTRY POINT
# ================================================================

if __name__ == "__main__":
    main()
