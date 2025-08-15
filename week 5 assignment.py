
# ============================
# Activity 1: Design Your Own Class 🏗️
# ============================

# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand          # Public attribute
        self.model = model
        self.__storage = storage    # Private attribute (encapsulation)
        self.battery = battery

    # Method to display smartphone info
    def show_info(self):
        print(f"{self.brand} {self.model} - {self.__storage}GB, Battery: {self.battery}mAh")

    # Method to use storage safely
    def use_storage(self, gb_used):
        if gb_used <= self.__storage:
            self.__storage -= gb_used
            print(f"Used {gb_used}GB. Remaining storage: {self.__storage}GB")
        else:
            print("Not enough storage!")

# Derived class: Smartphone with Camera (Inheritance & Polymorphism)
class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixels):
        super().__init__(brand, model, storage, battery)  # Initialize parent class
        self.camera_megapixels = camera_megapixels

    # Overridden method (Polymorphism)
    def show_info(self):
        print(f"{self.brand} {self.model} - {self.camera_megapixels}MP Camera, Battery: {self.battery}mAh")

    def take_photo(self):
        print(f"Click! Photo taken with {self.camera_megapixels}MP camera.")

# Create objects for Activity 1
print("=== Activity 1: Smartphones ===")
phone1 = Smartphone("Samsung", "Galaxy A52", 128, 4500)
phone2 = CameraPhone("Apple", "iPhone 14", 256, 3800, 48)

# Using methods
phone1.show_info()
phone1.use_storage(30)
print()
phone2.show_info()   # Overridden method
phone2.take_photo()
phone2.use_storage(50)  # Inherited method

print("\n" + "="*50 + "\n")

# ============================
# Activity 2: Polymorphism Challenge 🎭
# ============================

# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # To be implemented by child classes

# Derived classes with different move() implementations
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Create a list of vehicles
vehicles = [Car(), Plane(), Bicycle(), Boat()]

# Demonstrate polymorphism
print("=== Activity 2: Vehicle Movements ===")
for v in vehicles:
    v.move()
