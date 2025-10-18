class Member:
    def __init__(self, name: str, member_id: int, email: str):
        self.name = name
        self.member_id = member_id
        self.emial = email
        self.borrowed_book = []
        print(self.borrowed_book)

    def borrow_book(self, book: str):
        self.book = book
        self.borrowed_book.append(book)

    def return_book(self, book: str):
        self.book = book
        self.borrowed_book.remove(book)

    def show_info(self):
        print(
            f"Member name:{self.name} MemberID:{self.member_id} Member Email:{self.emial}"
        )
        print("List of Borrowed Books".center(50, "-"))
        for i, book in enumerate(self.borrowed_book, start=1):
            print(f"{i}. |{book}|")


class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_books += 1
        self.is_borrows = False

    def mark_as_borrowed(self):
        pass

    def mark_as_returend(self):
        pass

    def display_info(self):
        pass


class Library(Book):
    def __init__(self, name: str):
        super().__init__(self.title, self.author)
        self.name = name
        self.books = []
        self.members = []

    def add_book(self):
        self.books.append({"Title": self.title})

    def show_all_books(self):
        print(self.books)


# a = Member("Ali", 1, "ali@a.com")
# a.borrow_book("binavayan")
# a.borrow_book("100 sal tanhayie")
# a.borrow_book("I B4 U")
# a.return_book("binavayan")
# a.show_info()

b = Library("Meli")
b.add_book("Iran")
b.add_book("Tehran")
b.show_all_books()
