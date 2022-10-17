print("Edwin")
print("20")

pet_name = "Jeff"
pet_age = 2

print(pet_name)
print(pet_age)

total_price = 0
amoungus = 12
eldenring =60
projectgrove = 20
us_tax = 1.14

total_price += (amoungus + eldenring + projectgrove)
total_price *= us_tax

print("Your total price is: $" + str(total_price))

#exercise 4
name = "My name"
print("Your name is %s" % (name))
###
age = 12
height = 1.68

print("Your name is %s, your age is %d and your are %f cm tall" % (name, age, height))

name = "My name"
print("Your name is {}".format(name))

age = 12
height = 1.6867

print("Your name is{}, your age is {} and you are {:.2f} tall".format(name, age, height))

number = int(input("Give me a number: "))
print(number)

#erersice 6

number =  int(input("Give me a number: "))

if number < 100:
    print("That's a small number")
elif number <= 1000:
    print ("That's not a big number yet")
else:
    print("That's a big number")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")