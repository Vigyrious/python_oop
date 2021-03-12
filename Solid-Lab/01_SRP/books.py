char = "a"


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0



class Library:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def turn_page(book: Book):
        book.page += 1
        return
