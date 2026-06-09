class library:
    def __init__(self):
        self.noBooks = 0
        self.books =[]
    def addBook(self , book):
        self.books.append(book)
        self.noBooks = len(self.books)
    def showInfo(self):
        print(f"the library has {self.noBooks}  books")
l1 = library()
l1.addBook("Harry Potter")
l1.addBook("who i am")
l1.addBook("reble")
l1.showInfo()