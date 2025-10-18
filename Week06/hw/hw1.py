class Member:
    def __init__(self, name: str, member_id: int, email: str):
        self.name = name
        self.member_id = member_id
        self.emial = email
        self.borrowed_book = []

    def borrow_book(self, book: str):
        self.book = book
        self.borrowed_book.append(book)

    def show_borrowed(self):
        print(self.borrowed_book)

    def return_book(self, book: str):
        self.book = book
        self.borrowed_book.remove(book)


a = Member("Ali", 1, "ali@a.com")
a.borrow_book("binavayan")
a.borrow_book("100 sal tanhayie")
a.show_borrowed()
a.return_book("binavayan")
a.show_borrowed()
