class Student:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand}, {self.model} engine started!"
    

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def start(self):
        # print(f"{super().start()} doors: {self.doors}")
        print(f"{Vehicle.start(self)} doors: {self.doors}")

a = Car("GUGU", "BGU", 6)
a.start()