class Person:
    def __init__(self, first_name, last_name, age):
        self.first = first_name
        self.last = last_name
        self.age = age

    def description(self):
        print(f"{self.first} {self.last}, {self.age}")

    def birthday(self):
        self.age = self.age + 1
