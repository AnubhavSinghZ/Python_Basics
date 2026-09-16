class Car:
    color="white"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(Car): # Inheritance
    def __init__(self, name):
        self.name=name
car1=ToyotaCar("Fortuner")
car2=ToyotaCar("Hyryder")

print(car1.start())
print(car2.stop())
print(car1.color)