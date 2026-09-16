class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(Car):
    def __init__(self, name):
        self.name=name
car1=ToyotaCar("Fortuner")
car2=ToyotaCar("Hyryder")

print(car1.start())