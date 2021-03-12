from Person.person import Person


class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

