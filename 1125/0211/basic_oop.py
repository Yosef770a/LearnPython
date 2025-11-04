class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("There is not enough money left")

    def get_balance(self):
        return self.balance
    
# account_yemot = BankAccount(122770, 770)
# print(account_yemot.balance)
# account_yemot.deposit(18)
# print(account_yemot.balance)
# account_yemot.withdraw(88)
# print(account_yemot.balance)



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)

# recta = Rectangle(2, 3)
# print(recta.area())
# print(recta.perimeter())


import statistics
class Student:
    def __init__(self, name, grades: list):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return statistics.mean(self.grades)

# yossi = Student("yossi", [40])
# yossi.add_grade(35)
# print(yossi.grades)
# yossi.add_grade(35)
# yossi.average
# print(yossi.average())


class Book:
    def __init__(self, title, author, pages, is_read = False):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read

    def mark_as_read(self):
         self.is_read = True

    def info(self):
        print(f"Book Title: {self.title} , Author: {self.author}, Number of Pages: {self.pages}")
        if self.is_read:
            print("The book has been read")
        else:
            print("The book is not read")
        

# book1 = Book("The Lord of the Rings","John Ronald Reuel Tolkien", 1183)
# book1.info()
# book1.mark_as_read()
# book1.info()


# class Counter:
