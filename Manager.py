from Car import Car

class Manager(object):
    cars = []

    def __init__(self, cars):
        self.cars = cars

    def output_cars(self):
        i = 1
        for car in self.cars:
            print str(i) + "."
            i += 1
            print "Make: " + car.make
            print "Model: " + car.model
            print "Driven kms: " + str(car.driven_kms)
            print "Date of last service: " + car.last_service

    def edit_kilometers(self):
        i = int(raw_input("Select the  number of the car: "))
        kms = raw_input("Imput new kilometers value: ")

        if i <= len(self.cars) and i > 0:
            self.cars[i -1].driven_kms = kms

    def edit_last_service(self):
        i = int(raw_input("Select the  number of the car: "))
        d = raw_input("Enter day: ")
        m = raw_input("Enter month: ")
        y = raw_input("Enter year: ")

        if i <= len(self.cars) and i > 0:
            self.cars[i -1].set_last_service_date(d, m, y)

    def add_new_car(self):
        make = raw_input("Enter cars make: ")
        model = raw_input("Enter cars model: ")
        kms = float(raw_input("Enter cars kilometers: "))
        service = raw_input("Enter cars last service day: ")

        car_object = Car(make, model, kms, service)
        self.cars.append(car_object)

    def delete_car(self):
        i = int(raw_input("Select the  number of the car: "))
        self.cars.pop(i - 1)

    def write_to_file(self):
        file = open("cars.csv", "w+")
        for car in self.cars:
            file.write(car.make + "," + car.model + "," + car.driven_kms + "," + car.last_service)

    def read_from_file(self):
        file = open("cars.csv", "r")

        for line in file:
            values = line.split(",")
            car = Car(values[0], values[1], values[2], values[3])
            self.cars.append(car)

