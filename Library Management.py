import datetime

class Book:
    def __init__(self,title,author,book_id):
        self.title=title
        self.author=author
        self.book_id=book_id
        self.borrowed_by=None
        self.available=True
        self.due_date=None

class User:
    def __init__(self,user_id,name):
        self.name=name
        self.user_id=user_id
        self.borrowed_books=[]

class Library:
    def __init__(self):
        self.books={}
        self.user={}

    def add_book(self,title,author,book_id):
        self.books[book_id]=Book(title,author,book_id)
        print("Book added Succesfully")

    def register_user(self,user_id,name):
        self.user[user_id]=User(user_id,name)
        print("User registerd succesfully")

    def borrow_book(self,user_id,book_id):
        if book_id not in self.books:
            print("Book not found")

        if user_id not in self.user:
            print("User not found")
        book=self.books[book_id]
        user=self.user[user_id]

        if not book.available:
            print("Book is already borrowded")
        else:
            book.available=False
            book.borrowed_by=user_id
            book.due_date=datetime.date.today()+datetime.timedelta(days=7)
            user.borrowed_books.append(book_id)
            print(f"Book borrwed succesfully.Due date is {book.due_date}")

    def return_book(self,book_id,user_id):
        if book_id not in self.books or user_id not in self.user:
            print("Invalid user or book")
            return
        
        book=self.books[book_id]
        user=self.user[user_id]

        if book_id not in user.borrowed_books:
            print("user didn't borrow this book")
            return
        today=datetime.date.today()

        if today > book.due_date:
            days_late=(today-book.due_date).days
            penalty=days_late*5
            print(f"Book returned late.penalty{penalty}")
        else:
            print("Book returned on time or before !")
        book.borrowed_by=None
        book.available=True
        book.due_date=None
        user.borrowed_books.remove(book_id)

    def show_available_books(self):
        found=False
        for book in self.books.values():
            if book.available:
                found=True
                print(f"{book.book_id}:{book.title} by {book.author}")

        if not found:
                print("No available books")

library=Library()

while True:
    print("======LIBRARY SYSTEM=======")
    print("1.Add book")
    print("2.Register user")
    print("3.Borrow book")
    print("4.Return book")
    print("5.Available books")
    print("6.Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        x=input("Enter book title:")
        y=input("Enter author name:")
        z=int(input("Enter book id:"))
        library.add_book(x,y,z)

    elif choice=="2":
        y=input("Enter user name:")
        z=int(input("Enter user id:"))
        library.register_user(z,y)

    elif choice=="3":
        y=int(input("Enter book id:"))
        z=int(input("Enter user id:"))
        library.borrow_book(z,y)

    elif choice=="4":
        y=int(input("Enter book id:"))
        z=int(input("Enter user id:"))
        library.return_book(y,z)

    elif choice=="5":
        library.show_available_books()

    elif choice=="6":
        print("Thank you for using library system!")
        break

    else:
        print("Invalid choice try again")