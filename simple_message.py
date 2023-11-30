# part 1

# simple message
message = "this is my message"

print(message)

# simple messages
message = "now the messages is this"

print (message)

# personal message

name = "ringo    "

print("Hello " + name.strip().title() +", would you like to learn some Python today?")

# name cases

print("uppercase name is " + name.upper())
print("lowercase name is " + name.lower())
print("title name is " + name.title())

# Part 2

# names

friendslist = ["Mesha", "Yushan", "Jenna", "Mirela"]
print(friendslist)
print(friendslist[0])
print(friendslist[1])
print(friendslist[-2])
print(friendslist[-1])

#  greetings

print("Hi," + friendslist[0] + "! How are you finding this Python lab?")

# own list

carlist = ["Tesla S", "Tesla X", "Ford Fiesta"]

print(f"These are cars: {carlist[1]}." )

# guest list

guestlist = ["Mesha","Jack","Mirela"]

print(f"Dear, {guestlist[0]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")

# changing guest list

print(f"{guestlist[1]} cannot come.")
guestlist = ["Mesha","Chibuzor","Mirela"]

print(f"Dear, {guestlist[0]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")
print(f"Dear, {guestlist[1]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")
print(f"Dear, {guestlist[2]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")


# more guests

print("We're going to need a bigger boat.")

guestlist.insert(0,"Jack")
guestlist.insert(2,"Jenna")
guestlist.append("Yushan")

print(f"Dear, {guestlist[0]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")
print(f"Dear, {guestlist[1]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")
print(f"Dear, {guestlist[2]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")
print(f"Dear, {guestlist[3]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")
print(f"Dear, {guestlist[4]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")
print(f"Dear, {guestlist[5]}! You are invited for dinner.\n BYOB \n Love, Ringo \n")


# special

print("Dear, ", *guestlist,"! You are invited for dinner.\n BYOB \n Love, Ringo \n")

seplist= (*guestlist,sep=',')
print("Dear, ", seplist, "! You are invited for dinner.\n BYOB \n Love, Ringo \n")
#
# # shrinking guest list
#
# print(" I can only invite two guest oh nooo")
#
# del_guest = guestlist.pop()
# print(f"sorry {del_guest}, you have been eliminated")
#
# del_guest = guestlist.pop()
# print(f"sorry {del_guest}, you have been eliminated")
#
# del_guest = guestlist.pop()
# print(f"sorry {del_guest}, you have been eliminated")
#
# del_guest = guestlist.pop()
# print(f"sorry {del_guest}, you have been eliminated")
#
#
# print(f"Dear, {guestlist[0]}! You are still invited for dinner.\n BYOB \n Love, Ringo \n")
# print(f"Dear, {guestlist[1]}! You are still invited for dinner.\n BYOB \n Love, Ringo \n")
#
# del guestlist[0]
# del guestlist[0]
#
# print(f"guestlist is now empty: {guestlist}")
#
#


