 
# Exercise 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass


cat1 = Bengal("Milo", 3)
cat2 = Chartreux("Luna", 2)
cat3 = Siamese("Simba", 1)

all_cats = [ cat1, cat2, cat3]
sara_pets = Pets(all_cats)
sara_pets.walk()

# Exercise 2

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age 
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age*10
    
    def fight(self, other):
        power = self.run_speed() * self.weight
        power_other = other.run_speed() * other.weight
        if power < power_other :
            return f"{self.name} won the fight"
        elif power > power_other:
            return f"{other.name} won the fight"
        else:
            return "It's a tie"

dog1 = Dog("max", 5, 7)
dog2 = Dog("rex",8, 7)
dog3 = Dog("mal", 6, 9)

print(dog1.run_speed())
print(dog1.fight(dog2))

# Exercice 3

class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
   
    def born(self, **kwargs):
         self.members.append(kwargs)
         print(f"Congratulations to the {self.last_name} family!")
    def is_18(self, name):
         for member in self.members:
          if member["name"] == name:
              return member["age"] > 18
          return False
    def family_presentation(self):
        print(f"family name is {self.last_name}")
        for member in self.members:
            print(member)


members = [
    {"name": "Sara", "age": 25, "gender": "female"},
    {"name": "Adam", "age": 15, "gender": "male"}
]

family = Family(members, "Alami")

family.born(name="Lina", age=0, gender="female")

print(family.is_18("Sara"))
print(family.is_18("Adam"))

family.family_presentation()
