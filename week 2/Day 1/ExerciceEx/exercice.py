 
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