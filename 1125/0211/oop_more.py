class Book:
    def __init__(self,id, title, author, is_available = True):
        self.id = id
        self.title = title
        self.author = author
        self.is_available = is_available


    def unavailable_mark(self):
        if self.is_available:
            self.is_available = False
        else:
            print("The book has already been marked as unavailable")

        
    def available_mark(self):
        self.is_available = True



class Member:
    def __init__(self, id, full_name, active_loans_count = 0):
        self.id = id
        self.full_name = full_name
        self.active_loans_count = active_loans_count


    def loans_increment(self):
        self.active_loans_count += 1

    def loans_decrement(self):
        if self.active_loans_count:
            self.active_loans_count -= 1
        else:
            print("Cannot download less than 0")


class Loan:
    def __init__(self, loan_id, book_id, member_id, open_date):
        self.loan_id = loan_id
        self.book_id = book_id
        self.open_date = open_date
        self.member_id = member_id
        self.status =  "Open"
        self.date_return = None
        
    def close(self,return_date):
        if self.status == "Open":
            self.status =  "Closed"
            self.date_return = return_date
        else:
            print("It is not possible to close a loan that has already been closed")




class Library:
    def __init__(self, book: Book, member: Member, loan: Loan):
        self.book = book
        self.member = member
        self.loan = loan

    def add_book(self):
        Book(self.book)

    def add_member(self):
        Member(self.member)

    # def borrow(self,book_id, member_id, date):

aa = Library.add_book(770, "GUJGU", "VFFFFF")

print(aa)


        
        


