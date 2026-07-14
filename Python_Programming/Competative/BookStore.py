class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        BookStore.Name = Name 
        BookStore.Author = Author

        BookStore.NoOfBooks += 1

        
    def Display(self):
        print("Book Name : ",self.Name,", By Author : ",self.Author,"\nNo. of Books : ",self.NoOfBooks)

obj1 = BookStore("Linux System Programming","Robert Love")
obj1.Display()

obj2 = BookStore("C Programming","Dennis Ritche")
obj2.Display()