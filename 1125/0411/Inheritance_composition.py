from abc import ABC, abstractmethod
import math



class Vehicles:
    def __init__(self, max_speed):
        self.max_speed = max_speed
    
    def drive(self):
        print(f"This vehicles reaches a speed of {self.max_speed}")


class Car(Vehicles):
    def __init__(self, max_speed = 220):
        super().__init__(max_speed)


class Motorcycle(Vehicles):
    def __init__(self, max_speed = 120):
        super().__init__(max_speed)

 
# car1 = Car()
# car1.drive()
# moto1 = Motorcycle()
# moto1.drive()


#2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def manage(self):
        print(f"{self.name} is a manager")



class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def write_code(self):
        print(f"The programmer is {self.name}")


# developer = Developer("Yosef", 24000)
# manage = Manager("Yossi", 27000)

# developer.write_code()
# manage.manage()


# class Shape:
#     def __init__(self):
#         pass
    
#     def area(self):
#         pass



class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, wid, hei):
        self.wid = wid
        self.hei = hei

    def area(self):
        return self.wid * self.hei


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius * self.radius)


class Square(Shape):
    def __init__(self, surface):
        self.surface = surface

    def area(self):
        return self.surface * self.surface

# rectangle = Rectangle(4, 5)
# circle = Circle(3)
# square = Square(6)
# print(rectangle.area())
# print(circle.area())
# print(square.area())



class Payment:
    def __init__(self, method_name):
        self

class CreditCardPayment:
    def __init__(self, method_name):
        pass
