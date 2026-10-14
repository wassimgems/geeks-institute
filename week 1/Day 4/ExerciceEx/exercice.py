
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
# exercice 6
def make_shirt(size = "large" ,text = " i love python "):
    print (f"the size of the shirt is {size} and the text is {text}")

make_shirt()
make_shirt("medium")
make_shirt(size="medium", text="Hello World")

# exercice 7
def get_random_temp(season):
   def get_random_temp(season):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "spring":
        return random.randint(5, 25)
    elif season == "summer":
        return random.randint(20, 40)
    elif season == "autumn" or season == "fall":
        return random.randint(10, 30)
    else:
        return None

def main():
    season = input("enter a season :")
    
    tem = get_random_temp(season)
    print(f"the temperature right now is {tem} degrees celsius.")
    if tem < 0 :
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif tem  <= 16:
        print("quite chilly ! don t forget your coat")
    elif tem <= 23:
        print("The weather is mild. Enjoy your day!")
    elif tem <= 32:
        print("It's warm outside!")
    else:
         print("It's hot! Stay hydrated.")

main()

    #exercice 8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

wrong_answers = []
correct = 0
incorrect = 0

def ask ():
    for i in data:
       print(i["question"])
       user_answer = input("your answer : ")
       if user_answer == ["answer"]:
           print("correct")
           correct=+1
       else:
           print("incorrect")
           wrong_answers.append(user_answer)
           incorrect=+1

    

    
    
