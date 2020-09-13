class Lot:
    def __init__(self, capacity, price):
        self.capacity = capacity
        self.price = price

class Vehicle:
    def __init__(self, size="standard"):
        self.size = size

class Car(Vehicle):
    def __init__(self, size):
        super().__init__(size):
        self.

