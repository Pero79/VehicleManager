from Car import Car
from Manager import Manager


cars = []
manager = Manager(cars)
manager.read_from_file()

while True:
    print "_____________________"
    print "Choose (1-6)"
    print "1. Output all cars"
    print "2. Edit driven kilometers"
    print "3. Edit date of service"
    print "4. Add new car"
    print "5. Delete car"
    print "6. Close program"


    choice = raw_input()

    if choice == "1":
        manager.output_cars()
    elif choice == "2":
        manager.edit_kilometers()
    elif choice == "3":
        manager.edit_last_service()
    elif choice == "4":
        manager.add_new_car()
    elif choice == "5":
        manager.delete_car()
    elif choice == "6":
        with open("ListOfCars.txt", "w+") as ListOfCars:
            ListOfCars.write("This is the list of your cars:\n\n")
            i = 1
            for index, Car in enumerate(cars):
                ListOfCars.write(str(
                    i) + "| " + str(Car.make) + " " + str(Car.model) + " with " + str(Car.driven_kms) + " kilometers on the clock. Last serviced: " + str(Car.last_service))
                i += 1
            ListOfCars.write("\n\nList created with Vehicle Manager (v1.0)")
        print "Program closed all saved to file. ListOfCars.txt you can print, cars.csv is your database file.\n=====================\n"
        manager.write_to_file()
        break
    else:
        print "Enter value between 1-6\n**************************\n"

