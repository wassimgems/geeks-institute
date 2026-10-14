
# exercice 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print (dict(zip(keys,values)))

# exercice 2

family = {}
number = int(input("How many family members :"))

for i in range(number):
    name = input("entre your name :")
    age = int(input("entre your age : "))
    family[name] = age

totalprice = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age >= 12:
        price = 10
    else:
        price = 15

    print(f"{name} has to pay {price}")
    totalprice += price

print(f"totale price est {totalprice}")

#exercice 3

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}
more_on_zara = {
  'creation_date': "1975",
  'number_stores': "10000"
}

brand ['number_stores'] = 2
print(f" clients zaras are {brand['type_of_clothes'][0]} and {brand['type_of_clothes'][1]} and {brand['type_of_clothes'][2]} .")
brand ["country_creation"] = 'spain'
if 'intrenational_competitors' in brand :
    brand ['international_competitors'].append('desigual')

del brand ['creation_date']
print(brand ['international_competitors'][2])
print(brand['major_color']['US'])
print(len(brand))
for keys in brand.keys():
    print(keys)
brand.update(more_on_zara)
print(brand['number_stores'])
# l valeur dyal number_stores tbalat man 2 l 10000 

# exercice 4

def describe_city (city,country = 'ard'):
     print(f"{city} is in {country}")  

describe_city('rabat')
    
# exercice 5

import random ;

def numbers (num):
    ran_number = int((random.random()*100) + 1)
    if num == ran_number :
        print("success message")
    else:
        print(f"fail message your number is {num} and the random number is {ran_number}")

numbers()


