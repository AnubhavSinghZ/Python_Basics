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
