class Car:

    # make some attributes
    name = 'e323'
    make = 'Mercedes'
    model = 2009

    # make some methods
    def start(self):
        print('Start the engine')

    def stop(self):
        print('Stop the engine')

car_a = Car()
car_b = Car()
print(car_a.model)
print(type(car_a))
car_b.start()
car_a.stop()
print(dir(car_a))