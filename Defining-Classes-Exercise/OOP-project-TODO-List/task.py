class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if new_name == self.name:
            return f"Name cannot be the same."
        self.name = new_name
        return self.name


    def change_due_date(self, new_date):
        if new_date == self.due_date:
            return f"Date cannot be the same."
        self.due_date = new_date
        return self.due_date


    def add_comment(self, comment):
        self.comments.append(comment)
        return self.comments


    def edit_comment(self, comment_numbers, new_comment):
        if 0 <= comment_numbers < len(self.comments):
            self.comments[comment_numbers] = new_comment
            return ', '.join(self.comments)
        return "Cannot find comment."


    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

