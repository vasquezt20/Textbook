#Tyler Vasquez
#Textbook

from Textbook import Textbook

book1 = Textbook
book1.title = input("What is the book title?")
book1.author = input("What is the author's name?")
book1.price = input("What is the price?")
book1.quantity = input("What is the quantity?")

menu_choice = 0

while menu_choice != 4:
    print("What would you like to do?")
    print("1: Add inventory")
    print("2: deduct inventory")
    print("3: Modify the price")
    print("4: Quit")

    menu_choice = int(input())

    if menu_choice == 1:
        print("Book 1 or 2?")
        choice = int(input())
        if choice == 1:
            qty = int(input("How many are you adding?"))
            book1.add_inventory(qty)
            print("There is now " + str(book1.quantity) + "\n\n")
    elif menu_choice == 2:
        qty = int(input("How many are you removing?"))
        result = book1.deduct_inventory(qty)
        if result == 0:
            print("There is now 1" + str(book1.quantity) + "\n\n")
        else:
            print("You do not have enough")
    elif menu_choice == 3:
        price = float(input("What is the new price?"))
        book1.price = price
        print("The price of " + book1.title + " has been changed to " + str(book1.price) + "\n\n")
    elif menu_choice == 4:
        print("Thank you")
    else:
        print("ERROR")

