class Member:
    def __init__(self, name: str, member_id: int, email: str):
        self.name = name
        self.member_id = member_id
        self.emial = email
        self.borrowed_book = []

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


a = Member("Ali", 1, "ali@a.com")
a.borrow_book("binavayan")
a.borrow_book("100 sal tanhayie")
a.borrow_book("I B4 U")
a.return_book("binavayan")
a.show_info()
