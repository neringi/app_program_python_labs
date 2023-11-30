# Python Lab for Week 9 Classes and OOP


import time

# Part 1

#1. Classes: Create a new class called Car in a new Python script file (car.py). The class should have variables and methods.

# a. Define some variables to be initialised when creating an instance of a car (e.g., make, model, year,
# colour, registration_number). These are the attributes of car objects.

# class Car:
#     def __init__(self,make,model,year,colour,registration_number):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.colour = colour
#         self.registration_number = registration_number
#
# car_1 = Car("Ford", "fiesta",2006,"purple","AA56ABC")
#
# print(f"{car_1.make} {car_1.model}, made in {car_1.year}")


# b. Define and initialise other variables that are not passed when creating an instance (e.g., mileage = 0)

# class Car:
#
#     def __init__(self,make,model,year,colour,registration_number):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.colour = colour
#         self.registration_number = registration_number
#         self.mileage = 0
#
# car_2 = Car("Ford", "fiesta ghia",2007,"purple","AA57ABC")
#
# print(f"{car_2.make} {car_2.model}, made in {car_1.year}, mileage {car_2.mileage}")


# c. Define the class variable fleet_mileage to store to total mileage done by all the cars. This is a static
# variable

# class Car:
#
#     fleet_mileage = 0
#
#     def __init__(self,make,model,year,colour,registration_number):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.colour = colour
#         self.registration_number = registration_number
#         self.mileage = 0
#
#     def drive(self,distance):
#         self.mileage += distance
#         Car.fleet_mileage += distance
#         print(f"Distance travelled for {self.registration_number} is {distance}. New mileage is {self.mileage}")

# car_1 = Car("Ford", "fiesta",2006,"purple","AA56ABC")
# car_2 = Car("Ford", "fiesta ghia",2007,"purple","AA57ABC")

# car_1.drive(500)
# car_2.drive(1000)

# print(f"Car mileage is {car_1.mileage}, {car_2.mileage}")
# print(f"Fleet mileage is {Car.fleet_mileage}")

# d. Define a method called drive, which receives the distance to travel in a journey. The method must
# update the car mileage and the fleet_mileage class attribute. Print the reg_number, distance travelled
# and the actual mileage after driving.

# car_1.drive(1200)


# 2. Objects: Create a Python script file called car_fleet.py and import your car module


#
# Part 2
#

# 1. Inheritance. In this question, you will create child classes which inherit attributes and methods from the
# Car parent class.

# a. Modify the parent class. Define a method called display()to print the reg_number and mileage of a car.

class Car:

    fleet_mileage = 0

    def __init__(self,make,model,year,colour,registration_number):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.registration_number = registration_number
        self.mileage = 0

    def drive(self,distance):
        if self.mileage + distance <= 1000 :
            time.sleep(2)  # Halt the execution of the program for two seconds Part 3 1.
            self.mileage += distance
            Car.fleet_mileage += distance
            print(f"Distance travelled for {self.registration_number} is {distance}. New mileage is {self.mileage}")
        else: print(f"The maximum distance the car {self.registration_number} can travel is {1000-self.mileage}")

    def display(self):
        print(f"For registration number {self.registration_number}, the mileage is {self.mileage}")


# b. Choose two car makes and create two child classes from Car. Create a new Python script file per
# child class. Define the init method to initialise the class with all the arguments as done in the
# parent class except make. The constructor of the child class must call the init of the parent class
# and pass its make (e.g. Volkswagen). Keep in mind that you have to import the file where the parent
# class is defined. (e.g. import car)


# 2. Overriding methods: In this question, we will customise the display() method for some child classes.
# a. Define the display() method in one of your child classes and print a custom message, different to the
# one used in the Car class.
# b. Call the display() for all your Car objects in your main program and check that objects of the type Car
# and your child classes print different information using the same method. The display() method is
# overridden


# Part 4

# 1. Extending functionality of classes. If you want to explore more about advantages of using classes, you
# can complete the following exercise. Consider the condition: a car can travel a requested distance only if
# it hasn’t reached a maximum of 1000 miles in the odometer.

# a. Modify the drive method in the Car class to check if the Car meets the condition above
# ((mileage+distance) must be less than or equal to 1000). If the car can drive, update the mileage and
# print the remaining mileage. If the car cannot drive the entire journey, print a message to let the
# user know the maximum distance that a car can drive. If a car has reached the maximum mileage,
# print a custom message to say the car is out of service.

# b. Perform some journeys with cars from your main program and check that the validation works.
