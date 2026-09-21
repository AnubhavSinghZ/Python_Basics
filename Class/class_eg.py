# 1st Example 

# 1. Define the class blueprint
class Dog:
    # The constructor method initializes the attributes for every new dog
    def __init__(self, name, breed):
        self.name = name    # Instance variable unique to each dog
        self.breed = breed  # Instance variable unique to each dog

    # A method (function inside a class) to define an action
    def bark(self):
        return f"{self.name} says Woof!"

# 2. Create objects (instances) from the class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")





# 3. Access attributes and call methods
print(dog1.name)  # Output: Buddy
print(dog2.bark()) # Output: Max says Woof!




# 1. Define the class blueprint
class Car:
    # The constructor sets up the initial state of the car
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0  # All new cars start parked (0 mph)

    # Method to change the car's state (accelerate)
    def accelerate(self, mph_increase):
        self.speed += mph_increase
        return f"The {self.color} {self.model} accelerated to {self.speed} mph."

    # Method to check the current speed
    def check_speed(self):
        return f"Current speed: {self.speed} mph."

# 2. Create a car object
my_car = Car("Tesla", "Model 3", "Red")

# 3. Use the object's methods and modify its internal data
print(my_car.check_speed())       # Output: Current speed: 0 mph.
print(my_car.accelerate(45))      # Output: The Red Model 3 accelerated to 45 mph.
print(my_car.check_speed())       # Output: Current speed: 45 mph.

