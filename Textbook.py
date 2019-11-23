from Person import Person

class Textbook:
    def __init__(self, title, first, last, age, isbn, qty_in_inventory, price):
        self.title = title
        self.author = Person(first, last, age)
        self.isbn = isbn
        self.quantity = qty_in_inventory
        self.price = price

    def add_inventory(self, qty):
        self.quantity = self.quantity + qty

    def deduct_inventory(self, qty):
        if self.quantity >= qty:
            self.quantity = self.quantity - qty
            return 0
        else:
            return 1

    def reorder_warning(self):
        if self.quantity <= 5:
            return "TIme to reorder"
        else:
            return "Inventory"
