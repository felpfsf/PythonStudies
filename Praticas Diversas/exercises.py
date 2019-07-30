# name = input("Whats your name? ")
# # # age = input("Whats your age?")
# # # age = int
# age = int(input("How old are you? "))
# year = str((2019 - age)+100)
# print(name + " will turn 100 yo in " + year)

#Solution 2


import datetime

#ask age
name = input("Whats your name? ")

#ask age
age = input("How old are you? ")

#get current year
now = datetime.datetime.now()

#diference current year to 100
diff = 100 - int(age)

print(name + " you'll will complete 100 years old in", (now.year+diff))

#Exercise 2: Ask the number and tell if its even or odd

num = int(input("Pick a number: "))
check = int(input("Pick another number: "))
# mod = num % 2
# mod2 = num % check
# mod4 = num % 4
#
# if mod2 == 0:
#     print("it worked")
# else:
#     print("nope")
#
# if mod4 == 0:
#     print("mult 4")
# else:
#     print("not mult 4")
#
# if mod > 0 :
#     print("you pick an odd number")
# else:
#     print("you pick an even number")

if num % 4 == 0:
    print(num, " is a multiple of 4")
elif num % 2 == 0:
    print(num, " is an even number")
else:
    print(num, " is an odd number")

if num % check == 0:
    print(num, " divides evenly by ", check)
else:
    print(num, " doesnt divides by ", check)

#Exercise 3

import random
# a = [1, 1, 2, 5, 13, 21, 34, 55, 89]
b = []
tam = 10
for i in range(tam):
    b.append(random.randint(0, tam))

print(b)
print([bb for bb in b if bb < 5])
# print([aa for aa in a if aa < 5])
