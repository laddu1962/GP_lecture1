
# Exercise 3 - Physics class
# Temp (C) = (Temp(F) – 32) * 5/9
def f_to_c(f_temp):
    c_temp = (f_temp-32) * (5/9)
    return c_temp
print(f_to_c(156.2))


# Exercise 2 - safe cracker

import random

safe_code = []
# populate list
while len(safe_code) < 3:
    code = random.randint(3,12)
    if code not in safe_code:
        safe_code.append(code)

codes_cracked = 0

while codes_cracked < len(safe_code):
    for code in safe_code:
        print("enter number, that divide to %d" % code)
        try:
            guess = input("type 1st number")
            guess1 = input("type 2nd number")
            result = round(guess / guess1)
            if result == code:
                print("code cracked")
                codes_cracked += 1
        except ValueError:
            print("That is not the number")
            break;

else:
    print("You have opened the safe")


print(safe_code)


# Exercsie 1 - Zip Dictionaries

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = dict(zip(letters, points))
letter_to_points[""] = 0

total_points = 0
name = input('what is your name?:').upper()
new_list = []

for letter in name:
    if letter in letter_to_points and letter not in new_list:
        new_list.append(letter)
        total_points += letter_to_points[letter]


print("your name is worth %d points" % total_points)







