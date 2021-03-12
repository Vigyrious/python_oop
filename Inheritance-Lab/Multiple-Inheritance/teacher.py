from Person.person import Person
from Person.employee import Employee

class Teacher(Person, Employee):

    def teach(self):
        return f"teaching..."