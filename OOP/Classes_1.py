class Vehicle:
    def vehicle_method(self):
        print('Parent method of class Vehicle')


class Car(Vehicle):
    def car_method(self):
        print('Doter method of class Vehicle in class Car')


class Cycle(Vehicle):
    def cycle_method(self):
        print('Doter method of class Vehicle in class Cycle')


car = Car()
car.vehicle_method()

cycle = Cycle()
cycle.vehicle_method()
