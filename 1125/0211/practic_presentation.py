class Car:
    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year


    def get_car_info(self):
        return f"make: {self.make}, year: {self.year}, model: {self.model}"
    


new_car = Car("Byd", "Atto 3", 2023)
print("make", new_car.make)
print("model", new_car.model)
print("year", new_car.year)

print(new_car.get_car_info())

new_car.color = "black"
print(new_car.color)

del new_car.color
# print(new_car.color)
