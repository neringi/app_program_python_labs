from lab_5 import Car

# b. Choose two car makes and create two child classes from Car. Create a new Python script file per
# child class. Define the init method to initialise the class with all the arguments as done in the
# parent class except make. The constructor of the child class must call the init of the parent class
# and pass its make (e.g. Volkswagen). Keep in mind that you have to import the file where the parent
# class is defined. (e.g. import car)

class Tesla(Car):

    def __init__(self,model,year,colour,registration_number):
        super().__init__("Tesla", model, year, colour,registration_number)


car_10 = Tesla("S",2006,"purple","AA56ABC")

print(f" My car is {car_10.make} {car_10.model}")
