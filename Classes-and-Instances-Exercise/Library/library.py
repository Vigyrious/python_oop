
class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
            if user.username in self.rented_books:
                self.rented_books.pop(user.username)
        else:
            return f"We could not find such user to remove!"


    def change_username(self, user_id, new_username):
        person = [p for p in self.user_records if p.user_id == user_id]
        if person:
            if person[0].username == new_username:
                return"Please check again the provided username - it should be different than the username used so far!"
            if person[0].username in self.rented_books:
                self.rented_books[new_username] = self.rented_books[person[0].username].pop()
            person[0].username = new_username
            self.user_records.remove(person[0])
            self.user_records.append(person[0])
            return f"Username successfully changed to: {new_username} for userid: {user_id}"


        return f"There is no user with id = {user_id}!"


