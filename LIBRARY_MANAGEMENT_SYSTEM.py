#THIS CODE IS ABOUT IMPLEMENTING THE CONCEPTS OF OBJECT ORIENTED PROGRAMMING IN PYTHON...

'''THIS IS LIBRARY MANAGEMENT SYSTEM THAT DOES SIMPLE TASK LIKE DISPLAYING, 
ADDING, RETURNING, LENDING BOOKS USING STANDALONE FUNCTIONS.'''
class Library:    
    def __init__(self, booklist, libname):
        self.booklist = booklist
        self.libname = libname
        self.lend_rec ={}

    def displaybooks(self):
        print(f"This books are available : {self.booklist} at {self.libname}")

    def addbooks(self):
        book = input("Enter the book name you want to add to the Libraray: ")
        self.booklist.append(book)


    def lendbooks(self):
        book = input("Enter Book Name You want to Lend: ").capitalize()
        if book not in self.booklist:
            print("This book is not available at PPL.")
        if book in self.booklist:
            name = input("Enter lender name: ")
            self.booklist.remove(book)
            self.lend_rec[book] = name
        else:
            if self.lend_rec.get(book):
                print(f"This book was already booked by {self.lend_rec[book]}")

    def returnbooks(self):
        book = input("Enter the book name you want to return: ").capitalize()
        if book in self.lend_rec:
            print("Thank You for Returning the Book.\n")
            self.booklist.append(book)
            del self.lend_rec[book]

        else:
            print("This Book was not Lent\n")


booklist = ['A','B','C','D','E']
Smith_Library = Library(booklist, "Python Public Library")

while True:
    user = input("\nWelcome to Python Public Library [PPL] \n Input from the Following \n \"D\" for Display \n \"A\" for Adding \n \"L\" for Lending \n \"R\" for Returning \n \"Q\" for Quitting the Portal \n ")
    if user=="Q" or user=="q":
        break
    elif user=="D" or user=="d":
            Smith_Library.displaybooks()
    elif user=="A" or user=="a":
            Smith_Library.addbooks()
    elif user=="L" or user=="l":
            Smith_Library.lendbooks()
    elif user=="R" or user=="r":
            Smith_Library.returnbooks()
        




