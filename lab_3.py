favourite_movie = ['Cars','Shrek','Hocus Pocus', 'Clueless', 'Legally Blonde']

# 1. print favourite movies list

# print(favourite_movie)
#
# for i in favourite_movie:
#     print(f"Favourite movie is: {i}")
# input("What is your favourite movie?")

#  2. username list
# usernamelist = ['user1','user2','player1','admin','test']
#
# for i in usernamelist:
#     if i == 'admin':
#         print(f"Welcome {i}, do you want to view the status report?")
#     else:
#         print(f"Welcome {i}, thanks for logging in again.")

# 3. updated to make sure it handles no users!
# usernamelist = []

# if len(usernamelist) == 0:
#     print("No users exist.")
# elif len(usernamelist) > 0:
#     for i in usernamelist:
#         if i == 'admin':
#             print(f"Welcome {i}, do you want to view the status report?")
#         else: print(f"Welcome {i}, thanks for logging in again.")

# 4. check usernames

# current_users = ['User1','user2','player1','admin','test']
# new_users = ['player2','newuser1','newuser2','admin','user1']
#
# upper_current_users = [x.upper() for x in current_users]
# print(upper_current_users)
#
# for i in new_users:
#
#     if i.upper() in upper_current_users:
#         print(f"Username '{i}' is already taken. Please think of a different username.")
#     elif i.upper() not in upper_current_users:
#         print(f"Username '{i}' is available.")
#




# part 2

# 1. dictionary for a character

character = {
    "name": "player1",
    "age": "28",
    "height": "6ft",
    "rhand_equipment": "sword"
}

# 2. mob group

monsters = {
    "ogre": 2,
    "goblin": 3
}

for x,y in monsters.items():
    print(f"There are {y} {x}s.")


#get max value for monsters
    max_monster = max(monsters.values())
    print(max_monster)

#sort by key
for item in sorted(monsters.keys()):
    print(f"{item}")


# 2b. get max value
#sort by values backwards
    for item in reversed(monsters.values()):
        print(f"{item}")
        break

# 2c. get min value
# sort by values
for item in sorted(monsters.values()):
    print(f"{item}")
    break

# 3. glossary

monster_glossary = {
    "ogre": "Ogre is green and a low level monster to fight.",
    "goblin": "Goblins usually hang out in groups of atleast 3.",
    "imp": "Imps are tiny trickster fairies.",
    "wolf": "Wolves always fight in groups and surround their enemy.",
    "fae": "Fae are extremely easy to offend, be weary."
}

for x,y in monster_glossary.items():
    print(f"Monster:{x} \n Description: {y}")

# 4. inventory - list of dictionaries

inventory = {
    "dagger": {
        "name": "Thief's dagger",
        "value": 200,
        "desc": "Usually used by thieves. Small, sharp and pointy."
    },
    "healthPotion": {
        "name": "Health Potion",
        "value": 100,
        "desc": "A potion used to regenerate small amount of HP."
    },
    "goodHealthPotion": {
        "name": "Good Health Potion",
        "value": 150,
        "desc": "A potion used to regenerate a fair amount of HP."
    }
}

for x,y in inventory.items():
    print(f"Item: {x} \n Value: {}")