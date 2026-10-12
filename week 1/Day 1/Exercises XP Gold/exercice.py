
 # Exercise 1:

from random import random


month = int (input("Enter a mouth number:"))

if month > 3 and month < 5:
    print("spring")
elif month > 6 and month < 8:
    print("summer")
elif month > 9 and month < 11:
    print("autumn")
else:
    print("winter")


     # Exercise 2:




for i in range(1,21):
    if i % 2 == 0:
        print(i)


 # Exercise 3


 
 
user_name = input("Enter your name:")

while user_name !="wassim":
    print("the name is incorrect")
    user_name = input("Enter your name:")

print("hello wassim")


 # Exercise 4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user4_name = input("enter your name:")

if user4_name in names:
    while user4_name in names:
        names.remove(user4_name)

    names.insert(0, user4_name)
else:
    print("name not found")

print(names)

 # Exercise 5

number = int(input("Enter a number:"))
number2 = int(input("Enter a number 2:"))
number3 = int(input("Enter a number 3:"))

if number > number2 and number > number3:
    print ("the greatest number is :" +str(number))
elif number2 > number and number2 > number3:
    print("the greatest number is :" +str(number2))
elif number3 > number and number3 > number2:
    print ("the greatest number is :" +str(number3))
else:
    print("error")

# exercise 6

import random 

hnumber2 = int((random.random()*9)+1)
keep_gessing = True


while keep_gessing:
  number = int(input("Enter a number entre 1 et 9:"))
  if number == hnumber2 :
    print ("winner")
  else:
      print(" better luck next time")
  anser = input("you want to quit :")
  if anser == "yes":
     keep_gessing = False

print("1")




