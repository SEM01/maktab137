class Book:
    total_books = 0

    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.__is_borrowed = False
        Book.total_books += 1

    @property
    def is_borrowed(self):
        return self.__is_borrowed

    @property
    def isbn(self):
        return self.__isbn

    @is_borrowed.setter
    def is_borrowed(self, state):
        self.__is_borrowed = state

    def mark_as_borrowed(self):
        self.__is_borrowed = True

    def mark_as_returend(self):
        self.__is_borrowed = False

    def display_info(self):
        print(
            f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nIs Borrowed: {self.__is_borrowed}"
        )

    def book(self):
        return self.title

    def book_info(self):
        return self.title, self.author, self.isbn

    def book_isbn(self):
        return self.isbn


class Member:
    borrowed_book = []

    def __init__(self, name: str, member_id: int, email: str):
        self.name = name
        self.__member_id = member_id
        self.emial = email
        self.book = Book

    @staticmethod
    def borrow_book(self):
        if self.is_borrowed == True:
            print("Book is Borrowed")

    def return_book(self, book: str):
        self.book = book
        self.borrowed_book.remove(book)

    def show_info(self):
        print(
            f"Member name:{self.name}\nMemberID:{self.member_id}\nMember Email:{self.emial}"
        )
        print("List of Borrowed Books".center(50, "-"))
        print("No.\tBook Name")
        for i, book in enumerate(self.borrowed_book, start=1):
            print(f"{i}.\t|{book}|")

    def member_info(self):
        return self.name, self.member_id

    @property
    def member_id(self):
        return self.__member_id


class StudentMember(Member):
    def __init__(self, name, member_id, email):
        super().__init__(name, member_id, email)

    @staticmethod
    def borrow_book(self):
        if self.is_borrowed == True:
            print("Book is Borrowed")
        else:
            if len(Member.borrowed_book) < 3:
                Member.borrowed_book.append(Book.book(self))
            else:
                print("3 Book Limit Reached")


class TeacherMember(Member):
    def __init__(self, name, member_id, email):
        super().__init__(name, member_id, email)

    @staticmethod
    def borrow_book(self):
        if self.is_borrowed == True:
            print("Book is Borrowed")
        else:
            if len(Member.borrowed_book) < 5:
                Member.borrowed_book.append(Book.book(self))
            else:
                print("3 Book Limit Reached")


class Library:
    members = []
    books = []
    borrow_book_lst = []

    def __init__(self, name: str):
        self.name = name
        self.book = Book
        self.member = Member

    @staticmethod
    def add_book(self):
        Library.books.append(Book.book_info(self))

    @staticmethod
    def add_member(self):
        Library.members.append(Member.member_info(self))

    @staticmethod
    def borrow_book(self):
        if Book.book(self) not in Library.borrow_book_lst:
            if self.is_borrowed == True:
                Library.borrow_book_lst.append([Book.book(self)])

        else:
            print(f"'{Book.book(self)}' already Exist in the Borrow List")
        print(Library.borrow_book_lst)

    def return_book(self, member_id, isbn):
        pass

    def show_all_members(self):
        print("List of Members".center(50, "."))
        print("No.\tName\tMemebrID")
        for i, (name, ID) in enumerate(self.members, start=1):
            print(f"{i}.\t{name}\t{ID}")

    def show_all_books(self):
        print("List of Books".center(50, "."))
        print("No.\tTitle\t\tAuthor\t\tISBN")
        for i, (title, author, isbn) in enumerate(self.books, start=1):
            print(f"{i}.\t{title}\t\t{author}\t\t{isbn}")
        print(f"Total Books: {Book.total_books}")


a = Book("Book1", "Author1", 1)
b = Book("Book2", "Author2", 2)
c = Book("Book3", "Author2", 3)
d = Book("Book4", "Author2", 4)


k = StudentMember("std1", 1, "std1@1.com")
t = TeacherMember("tcr1", 110, "tcr1@2.com")
