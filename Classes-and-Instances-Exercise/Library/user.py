

class User:

    def __init__(self, id, username):
        self.user_id = id
        self.username = username
        self.books = []


    def get_book(self, author, book_name, days_to_return, library):
        if book_name in library.books_available[author]:
            library.books_available[author].remove(book_name)
            if self.username not in library.rented_books:
                library.rented_books[self.username] = {}
            library.rented_books[self.username].update({book_name: days_to_return})
            self.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for user, books in library.rented_books.items():
            for book, time in books.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {time} days!'




    def return_book(self, author, book_name, library):
        if book_name in self.books:
            self.books.remove(book_name)
            library.rented_books[self.username].pop(book_name)
            library.books_available[author].append(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"