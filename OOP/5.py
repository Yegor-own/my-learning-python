class Car:

    def __init__(self):
        print('Start the Engine')
        self.name = 'Corolla'
        self.__make = 'Toyota'
        self.__make = 1999

car_a = Car()
print(car_a.name)
