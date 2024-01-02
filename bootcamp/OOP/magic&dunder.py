mylist = [1,2,3]
class Book():
    def __init__(self,x,y,z):
        self.title = x
        self.author = y
        self.pages = z
    def __str__(self):
        return f"{self.title} by {self.author} with {self.pages} pages"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book has been deleted")
Book1 = Book("Python book", "Vasista", 324)
print(Book1.title)
print(Book1)
print(len(Book1))
# del Book1
# above method deletes the instance of the Book class
