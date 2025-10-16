class Book:
    def __init__(self, title, author, genre, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def borrow(self):
        if not self.available:
            return self.available
        else:
            self.available = False
