
player = {'Health': 20, 'Weapons': 0}
inventory = 0


text = """Hello minions welcome to your worst nightmare!
At Starbucks 0174! Filled with people. 
Then suddenly everyone turns into monsters
The staff room is on your left but you have to..."""

text2 = """Good job.
Imagine you forgot your password, that would have been an ugly ending.
All of this is happening because then Tentacle monster has been released from the drift!"""

text3 = """"The staff room has items which can be used as weapons!
The items in the room are...."""

test4 = "choice 2 items to defend yourself"

print(text)

password = "0174"
usrAttempts = 3


while usrAttempts > 0:
    guess = input("type password")
    if guess == password:
        print("door opened")
        break
    usrAttempts -= 1
else:
    print("not attempts left")

print(text2)
print(text3)

staff_room = {'broomstick': 5, 'butter Knife': 10, 'cup': 3, 'pumpkin spic latte': 30}
print(staff_room)

print(test4)

for k, val, in staff_room.itmes():
    print("You have picked up", k, "it has" val, "damage")


inventory = inventory + staff_room.pop(input())

#print(inventory)






# exercise 5
tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "TheEmperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot",
          8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death",
          14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun",
          20: "Judgement", 21: "The World", 22: "The Fool"}

fortune = {}

fortune["past"] = tarot.pop(13)
fortune["present"] = tarot.pop(22)
fortune["future"] = tarot.pop(10)

for k, val in fortune.items():
    print("your", k, "is the", val, "card")

import  random

fortune = {"past": "", "present": "", "future": ""}

for key in fortune.keys():
    remaining_cards = list(tarot.keys())
    choice = remaining_cards[random.randint(0, len(remaining_cards)-1)]
    fortune[key] = tarot.pop(choice)

for key, value in fortune.items():
    print("Your {} is the {} card." .format(key, value))



# exercise 4
available_items = {"health potion": 10, "cake": 5, "green elixir": 20, "lombas bread": 25, "bogweed": 15, "rabbit stew": 30}
health_points = 20

health_points += available_items.pop("bogweed")  # .pop means it return the value, modifies dictionary

print(health_points)



# exercise 3
animals_on_campus = {}

animals_on_campus['fox'] = 8
animals_on_campus['birds'] = 12
animals_on_campus['aligators'] = 0
print(animals_on_campus)
animals_on_campus['fox'] = 4
print(animals_on_campus)  # as multiple keys can't at exists once, thus the key will gets overwritten,



# exercise2
translation = {'mountain': 'blenon', 'bread': 'havon', 'friend': 'raqiros', 'horse': 'anne'}
print(translation['friend'])



# exercise1
print("type a list of numbers..")

user = input()
x = user.split()
# make a new list for the output
output = []

for number in x:
    if int(number) % 2 != 0:  # convert input into int
        output.append(number)

print(output)



