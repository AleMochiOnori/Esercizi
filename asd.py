class Book :
    def __init__(self , book_id , title , author , is_borrowed):
        self.book_id = book_id
        self.title = title 
        self.author = author
        self.is_borrowed = False


    def borrow(self) :
        if self.is_borrowed  is False:
            self.is_borrowed = True


    def return_book(self):
        return self.is_borrowed 
    
class Member :
    def __init__(self , member_id , name , borrowed_books : list[Book]):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books


    def borrow_book(self,book):
        if book.is_borrowed is False:
            self.borrowed_books.append(book)

    def return_book():
                