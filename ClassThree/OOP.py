'''
OOP en Python.
'''

class Car:
    def __init__(self, models: str, kms: int):
        self.Model = models
        self.Kms = kms

    def __repr__(self):
        return "CAR"
    
    def broom(self, distance: int):
        self.Kms += distance
    
# Testing
tes_car = Car("Rayo McQueen", 95)
print(tes_car)
tes_car.broom(100)
print(tes_car.Kms)
