import pickle


class Book:
    total_books = 0

    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        Book.total_books += 1

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returend(self):
        self.is_borrowed = False

    def display_info(self):
        print(
            f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nIs Borrowed: {self.is_borrowed}"
        )

    def borrow_check(self):
        return self.is_borrowed

    def book(self):
        return self.title

    def book_info(self):
        return self.title, self.author, self.isbn

    @staticmethod
    def book_isbn(isbn):
        return isbn


class Member:

    total_members = 0

    def __init__(self, name: str, member_id: int, email: str):
        self.name = name
        self.member_id = member_id
        self.emial = email
        self.book = Book
        Member.total_members += 1

    @staticmethod
    def borrow_book(book):
        if Book.mark_as_borrowed == True:
            print(f"{Book.book(book)} is borrowed")

    @staticmethod
    def return_book(book: str):
        pass

    def show_info(self):
        print(
            f"Member name:{self.name}\nMemberID:{self.member_id}\nMember Email:{self.emial}"
        )
        print("List of Borrowed Books".center(50, "-"))
        print("No.\tBook Name\tAuthor")
        for i, book in enumerate(self.borrowed_book, start=1):
            print(f"{i}.\t|{book[0]}|\t\t{book[1]}")

    def member_info(self):
        return self.name, self.member_id

    @staticmethod
    def member_no(id):
        return id


class StudentMember(Member):
    borrowed_book = []

    def __init__(self, name, member_id, email):
        super().__init__(name, member_id, email)

    @staticmethod
    def borrow_book(book):
        if Book.borrow_check(book) == True:
            print(f"{Book.book(book)} is borrowed")
        else:
            if len(StudentMember.borrowed_book) < 3:
                StudentMember.borrowed_book.append(Book.book_info(book))
            else:
                print("3 Book Limit Reached")

    @staticmethod
    def return_book(book):
        TeacherMember.borrowed_book.remove(Book.book_info(book))


class TeacherMember(Member):
    borrowed_book = []

    def __init__(self, name, member_id, email):
        super().__init__(name, member_id, email)

    @staticmethod
    def borrow_book(book):
        if Book.borrow_check(book) == True:
            print(f"{Book.book(book)} is borrowed")
        else:
            if len(TeacherMember.borrowed_book) < 5:
                TeacherMember.borrowed_book.append(Book.book_info(book))
            else:
                print("5 Book Limit Reached")

    @staticmethod
    def return_book(book):
        TeacherMember.borrowed_book.remove(Book.book_info(book))


class Library:
    members = []
    books = []
    borrow_book_lst = []
    return_book_lst = []

    def __init__(self, name: str):
        self.name = name
        self.book = Book
        self.member = Member

    @staticmethod
    def add_book(book):
        if Book.book_info(book) in Library.books:
            print(f"'{Book.book_info(book)[0]}' Exist")
        else:
            Library.books.append(Book.book_info(book))
        with open("library_data.pkl", "ab") as file:
            pickle.dump(f"Add Book: {Book.book_info(book)}", file)

    @staticmethod
    def add_member(member):
        if Member.member_info(member) in Library.members:
            print(f"'{Member.member_info(member)[0]}' Exist!")
        else:
            Library.members.append(Member.member_info(member))
        with open("library_data.pkl", "ab") as file:
            pickle.dump(f"Add Member: {Member.member_info(member)}", file)

    @staticmethod
    def borrow_book(member_id, isbn):
        if member_id in [x[1] for x in Library.members]:
            if isbn in [x[2] for x in Library.books]:
                Library.borrow_book_lst.append(
                    (Member.member_no(member_id), Book.book_isbn(isbn))
                )
            else:
                print(f"'{isbn}' is no valid")
        else:
            print(f"'{member_id}' is not member")
        with open("library_data.pkl", "ab") as file:
            pickle.dump(
                f"Book Borrowed: {Member.member_no(member_id), Book.book_isbn(isbn)}",
                file,
            )

    @staticmethod
    def return_book(member_id, isbn):
        if member_id in [x[1] for x in Library.members]:
            if isbn in [x[2] for x in Library.books]:
                Library.return_book_lst.append(
                    (Member.member_no(member_id), Book.book_isbn(isbn))
                )
            else:
                print(f"'{isbn}' is no valid")
        else:
            print(f"'{member_id}' is not valid")

    def show_all_members(self):
        print("List of Members".center(50, "."))
        print("No.\tName\tMemebrID")
        for i, (name, ID) in enumerate(self.members, start=1):
            print(f"{i}.\t{name}\t{ID}")
        print(f"Total Members: {Member.total_members}")

    def show_all_books(self):
        print("List of Books".center(50, "."))
        print("No.\tTitle\t\tAuthor\t\tISBN")
        for i, (title, author, isbn) in enumerate(self.books, start=1):
            print(f"{i}.\t{title}\t\t{author}\t\t{isbn}")
        print(f"Total Books: {Book.total_books}")

    @staticmethod
    def search_member_by_name(name):
        if name in [x[0] for x in Library.members]:
            print(f"'{name}' Find.")
        else:
            print(f"'{name}' not Found")

    @staticmethod
    def search_book_by_title(name):
        if name in [x[0] for x in Library.books]:
            print(f"'{name}' Find.")
        else:
            print(f"'{name}' not Found")

    @staticmethod
    def library_report():
        print(f"Borrowed: {len(Library.borrow_book_lst)}")
        print(f"Available: {(len(Library.books))-(len(Library.borrow_book_lst))}")

    @staticmethod
    def read_report(filename):
        result = []
        try:
            with open(filename, "rb") as file1:
                while True:
                    try:
                        a = pickle.load(file1)
                        result.append(a)

                    except EOFError:
                        break
                for i, item in enumerate(result, 1):
                    print(i, item)
            return result
        except FileNotFoundError:
            print("File not Fond")


a = Book("Book1", "Author1", 1)
b = Book("Book2", "Author2", 2)
c = Book("Book3", "Author3", 3)
d = Book("Book4", "Author4", 4)
e = Book("Book5", "Author5", 5)
f = Book("Book6", "Author6", 6)


s = StudentMember("std1", 1, "std1@1.com")
t = TeacherMember("tcr1", 110, "tcr1@2.com")

l = Library("Meli")
