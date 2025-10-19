class Book:
    total_books =0
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        Book.total_books +=1

    def mark_as_borrowed(self):
        self.is_borrowed = True
        

    def mark_as_returend(self):
        self.is_borrowed = False

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nIs Borrowed: {self.is_borrowed}")

    def book(self):
        return self.title


class Member:
    borrowed_book = []
    def __init__(self, name: str, member_id: int, email: str):
        self.name = name
        self.member_id = member_id
        self.emial = email
        self.book=Book
            
    @staticmethod   
    def borrow_book(self):
        if Book.mark_as_borrowed==True:
            print("Book is Borrowed")
        else:
            Member.borrowed_book.append(Book.book(self))

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
class StudentMember(Member):
    pass

class TeacherMember(Member):
    pass

       

class Library():
    members = []
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.member = Member

    def add_book(self, book):
        #TODO: self.books.append({"Title": self.title})
        pass
    @staticmethod
    def add_member(self):
        Library.members.append(Member.member_info(self))

    def borrow_book(self,member_id, isbn):
        pass

    def return_book(self, member_id, isbn):
        pass

    def show_all_members(self):
        print("List Of Members".center(50, "-"))
        print("No.\tName\tMemebrID")
        for i, (name, ID) in enumerate(self.members, start=1):
            print(f"{i}.\t{name}\t{ID}") 
        

    def show_all_books(self):
        print(self.books)


# a = Member("Ali", 1, "ali@a.com")
# a.borrow_book("binavayan")
# a.borrow_book("100 sal tanhayie")
# a.borrow_book("I B4 U")
# a.return_book("binavayan")
# a.show_info()

# b = Library("Meli")
# b.add_book("Iran")
# b.add_book("Tehran")
# b.show_all_books()

a = Book("Sovashon","Simin",123)
b = Book("a","b",12)
b.mark_as_borrowed()
# a.display_info()
f = Member("f",1,"a@a.com")
g= Member("g",1,"a@a.com")
f.borrow_book(a)
f.borrow_book(b)
f.show_info()
l = Library("meli")
l.add_member(f)
l.add_member(g)
l.show_all_members()
