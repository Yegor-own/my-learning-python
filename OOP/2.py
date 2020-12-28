class Car:

    car_count = 0

    def start(self, name, make, model):
        print('Start the engine')
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

car_a = Car()
car_a.start('Corolla', 'Toyota', 2015)
print(car_a.name, car_a.car_count)
car_b = Car()
car_b.start('City', 'Honda', 2013)
print(car_b.name, car_b.car_count)