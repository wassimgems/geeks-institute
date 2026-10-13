
# exercice 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print (dict(zip(keys,values)))

# exercice 2

family = {}
number = int(input("How many family members :"))

for 0 in range(number):
 name = input("entre your name :")
 age = input ("entre your age : ")
 family [name] = [age]

totalprice = 0

for name , age in family.items():
 if age < 3 :
  price = 0
 elif age >= 12 :
  price = 10
 else:
  price = 15
  print(f"{name} has to pay {price}")
  totalprice =+ price

print(f"totale price est {totalprice}")  




