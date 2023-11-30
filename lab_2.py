# 1. Conditional Tests

print(5>4)

print(5<4)

print(4==4)

print(20==4)

print("4"== 4)

print("hi" == 4)

print(0 < 1 < 3)

print("hi" == 'hi')

print(len("hi") == 2)

print(1 != 0)

print(1==1 or 0==1)

# 2. more conditional tests

a = "I AM NOT SHOUTING"
print(a.lower())

print(1==1 or 0==1)

print(1==1 and 0==1)

print(1 != 0)

print(1 != 1)

fruits = ["apples", "oranges", "pears"]

fruitA = "banana"

if fruitA in fruits:
    print("exist")
else:
    print("does not exist")


# 3. day number

weekday = "Wednesday"

if weekday.lower() == "monday": print(1)
elif weekday.lower() == "tuesday": print(2)
elif weekday.lower() == "wednesday": print(3)
elif weekday.lower() == "thursday": print(4)
elif weekday.lower() == "friday": print(5)
elif weekday.lower() == "saturday": print(6)
elif weekday.lower() == "sunday": print(7)
else: print("not a day of the week")

# 4. days in month

month28d = ["february"]
month30d = ["april","june","september","november"]
month31d = ["january","march","may","july","august","october","december"]

month = "february"
year = 2024

if month in month28d:
    if year % 4 == 0:
        print(f"Year {year} is a leap year")
        print("29 days in a month")
    elif year % 4 != 0:
        print(f"Year {year} is not a leap year")
        print("28 days in a month")
elif month in month30d:
    print("30 days in a month")
elif month in month31d:
        print("31 days in a month")
else: print("not a month")

# PART 2

# 1. name

# name = input("What is your name? ")
# print(name)

# 2. dinner guests
# guests = input("How many people are in the dinner group? ")
#
# if int(guests) > 8:
#     print("please wait for a table")
# else: print("follow me to be seated")

# 3. multiple of two

# number = input("think of a natural number...")
# if int(number) % 2 == 0:
#     print("Congratulations! Your number is even")
# else: print("Your number is odd")

# 4. cinema tickets


while True:
    try:
        age = int(input("what is your age?"))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        continue

    if age < 5: print("Free")
    elif age in range(5,12):
        print("£3")
    elif age in range(12, 65):
        print("£10")
    elif age > 65:
        print("£5")
    break




