# Assignment 1: Design Your Own Class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.__battery_life = battery_life  # encapsulated private attribute

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery Life: {self.__battery_life}h")

    def charge(self, hours):
        self.__battery_life += hours
        print(f"Charging... Battery life is now {self.__battery_life}h")

# Inheritance example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system

    def show_info(self):
        super().show_info()
        print(f"Cooling System: {self.cooling_system}")

# Testing Assignment 1
phone1 = Smartphone("Samsung", "Galaxy S23", 24)
phone1.show_info()
phone1.charge(5)

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 20, "Advanced Liquid Cooling")
gaming_phone.show_info()


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass  # base method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Polymorphism demonstration
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
