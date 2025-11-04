
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"The vehicle is moving {self.brand} {self.model}")



class Car(Vehicle):  
    def move(self):
        print("The car drives")



class Plane(Vehicle):
    def move(self):
        print("The plane flies")



# list_car = [("byd", "atto3"),("tesla", "model3")]
# for i in list_car:
#     car = Vehicle(i[0], i[1])
#     car.move()


list_car = [("byd", "atto3"),("tesla", "model3")]
for i in list_car:
    car = Car(i[0], i[1])
    car.move()

# a = Vehicle("fufuyfc", "guu")
# a.move()



class Animals:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "sound"

class Dog(Animals):
    def sound(self):
        return self.name + " Woof"
    

class Cat(Animals):
    def sound(self):
        return self.name + " Meow"
    
list_animals = [Dog("rexi"), Cat("jeck")]
for i in list_animals:
    print(i.sound())





class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    
class Managerbonus(Employee):
    def addsbonus(self, amount):
        self.salary += amount