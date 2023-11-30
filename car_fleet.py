# 2. Objects: Create a Python script file called car_fleet.py and import your car module.
# a. Create a fleet of five car objects with different information.

from lab_5 import *
from ford import *
from tesla import *

car_1 = Ford("fiesta",2006,"purple","AA56ABC")
car_2 = Ford("Mondeo",2011,"black","AA60DJU")
car_3 = Tesla("S",2020,"silver","AA70PAO")
car_4 = Tesla("E",2021,"red","AA71ALD")
car_5 = Ford("Titanium",2010,"red","AA00ASW")
car_6 = Car("Vauxhall","Corsa",2015,"black","AA12SAD")


# b. Call the drive method once for each car you created. Set the distance of your choice.

car_1.drive(100)
car_2.drive(200)
car_3.drive(500)
car_4.drive(0)
car_5.drive(250)
car_1.drive(200)

# c. Print the fleet_mileage static class variable and check that this equals the sum of the car journeys.
# fleet_mileage is a static class variable, so it’s shared among the objects

print(f"Car fleet mileage is {Car.fleet_mileage}")

car_1.display()
#
# d. Do some journeys (drive()) with your new car objects, print the fleet_mileage and check that the
# fleet mileage is updated and equals the sum of all car journeys.

car_1.drive(100)
print(f"Car fleet mileage is {Car.fleet_mileage}")


car_6.display()

car_1.drive(1000)




