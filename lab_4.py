# Lab 4 - functions

# Part 1

# 1. Message

# Write a function called display_message() that prints one sentence explaining something about Python.
# Call the function, and check it displays the message.

# def display_message():
#     print("Python is a programming language.")
#
#
# display_message()

# 2. Item

# Write a function called display_item() that receives an item name, and how much it cost (paramaters).
# The function must print a message about the item, and its value. Call the function once using positional
# arguments. Call the function a second time using keyword arguments

# def display_item(item_name, item_cost):
#     print(f"The item '{item_name.title()}' costs {item_cost} gold coins.")
#
# display_item("small potion", 10)
#

# 3. Expensive items

# Modify the function display_item() such that its default cost is 100. Make two items, one
# that uses the default price, and one that uses a set price. Call them to make sure it works.

#
# def display_item(item_name, item_cost=100):
#     print(f"The item '{item_name.title()}' costs {item_cost} gold coins.")
#
# display_item("small potion", 10)
# display_item("medium potion")

# 4. People

# Make a list of names. Pass the list to a function called show_people(). show_people() should
# print all the names in the list.

# people = ["Neringa", "Mesha", "Sylvia"]
#
# def show_people(names):
#     for name in names:
#         print(f"Hi {name.title()}")
#
# show_people(people)

# 5. Create a character

# Write a function called create_character() that creates a dictionary describing a player
# in a game. The function should take the character’s name, age, height, and weight (paramaters). The
# function should return a dictionary with these attributes set.

# def create_character(name, age, height, weight):
#
#     #create an empty character dictionary
#     character = {}
#
#     #character traits required
#     character["name"] = name.title()
#     character["age"] = age
#     character["height"] = height
#     character["weight"] = weight
#     print(character)
#
# create_character("player1", 20,"6ft2in","70kg")


# a. Extend create_character() to accept additional parameters. Consider hair colour, eye colour and
# gender.

# def create_character(name, age, height, weight, *attributes):
#
#     #create an empty character dictionary
#     character = {}
#
#     #character traits required
#     character["name"] = name.title()
#     character["age"] = age
#     character["height"] = height
#     character["weight"] = weight
#     character["other"] = []
#     for attribute in attributes:
#         character["other"].append(attribute)
#
#     print(character)
#
# create_character("player2", 25,"6ft2in","70kg","blue eyes","black hair")


# 6. User character

# Use your function from Q5. Write a while loop that allows users to enter different
# information for the characters. Collect the information from the user input, then call the create_character()
# function, which must print the dictionaries that have been created.

def new_character():

    character= {}

    while True:

        new_key= input("Add new trait type i.e. name, race, class, age, etc. Or enter 'q' to quit")
        if new_key == 'q':
            break

        print(f"Great! Character trait '{new_key}' added.")
        new_value= input("Now add specification for said trait type i.e. Player1, Elf, 150, etc. Or enter 'q' to quit")
        if new_value == 'q':
            break

        character[new_key] = new_value

        print(f"New character trait '{new_key}' added. You are {new_value}!")


        print(f"Your character is: ")
        print(character)

new_character()