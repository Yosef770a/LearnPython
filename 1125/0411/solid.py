import statistics 
from abc import ABC, abstractmethod
import math

#S1
class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
    def __str__(self):
        return f"title: {self.title}, author: {self.author}, content: {self.content}"

class Library:
    def __init__(self):
        self.books = []

    def save_to_list(self, book: Book):
        self.books.append(str(book))
        
    def print_list(self):
        print(self.books)
        
# book1 = Book("The Lord of the Ring", "J. R. R. Tolkien", "The Fellowship of the Ring..." )
# library1 = Library()
# library1.save_to_list(book1)
# library1.print_list()



#S2
class Student:
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = grades


class GradeCalculator:
    def __init__(self):
        pass

    @staticmethod
    def average_grade(grades: list):
        average = statistics.mean(grades)
        return average

# student = Student("Yossi", [48, 45])
# print(GradeCalculator.average_grade(student.grades))



#S3
class Order:
    def __init__(self, items: list,total_price: float):
        self.items = items
        self.total_price = total_price

class InvoicePrinter:
    def __init__(self):
        pass

    def print_invoice(self, order:Order):
        print(f"The order data is: Product list: {order.items} Total price: {order.total_price}")


# order = Order(["200 credits for sending SMS", "200 voicemail credits"], 58)
# invoice = InvoicePrinter().print_invoice(order)



#O1
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * (self.r * self.r)

class Square(Shape):
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a * self.a    
    
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

# rectangle = Rectangle(4, 5)
# circle = Circle(3)
# square = Square(6)
# print(rectangle.area())
# print(circle.area())
# print(square.area())


#O2
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"You have to pay: {self.amount}")

class CreditCardPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

class PayPalPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

class CryptoPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

# card_pay = CreditCardPayment(770)
# card_pay.pay()
# pal_pay = PayPalPayment(660)
# pal_pay.pay()
# crypto_pay = CryptoPayment(550)
# crypto_pay.pay()


#O3
class Notifier:
    def __init__(self, message):
        self.message = message

    def send(self):
        print(f"The message is: {self.message}")

class EmailNotifier(Notifier):
    def __init__(self, message):
        super().__init__(message)

class SMSNotifier(Notifier):
    def __init__(self, message):
        super().__init__(message)

class PushNotifier(Notifier):
    def __init__(self, message):
        super().__init__(message)


# mail_notifie = EmailNotifier("SAPM")
# mail_notifie.send()
# sms_notifie = SMSNotifier("SAPMSMS")
# sms_notifie.send()
# push_notifie = PushNotifier("Alert Oref")
# push_notifie.send()

#Liskov 1 (before proper use)
class BirdUnit:
    def __init__(self):
        pass

    def fly():
        print("can fly")
        

class Drone(BirdUnit):
    def __init__(self):
        super().__init__()

class Tank(BirdUnit):
    def __init__(self):
        super().__init__()

    def fly():
        print("should not fly")


# This implementation breaks the Liskov principle because we are inheriting and overriding a method from the parent class whose meaning is completely different from our actual usage.

#Liskov 2 (Correct implementation of the first part)
class BirdUnit:
    def __init__(self):
        pass

    def fly():
        print("can fly")

class GroundUnit:
    def __init__(self):
        pass

    def fly():
        print("should not fly")

class Drone(BirdUnit):
    def __init__(self):
        super().__init__()

class Tank(GroundUnit):
    def __init__(self):
        super().__init__()

