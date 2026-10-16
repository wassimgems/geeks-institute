
#exercice 2

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def oldest (cat1,cat2,cat3):
        if cat1.age > cat2.age > cat3.age:
            return  cat1
        elif cat2.age > cat1.age > cat3.age:
            return cat2
        else:
            return cat3         
cat1 = Cat("tom",4)
cat2 = Cat("wassim",5)
cat3 = Cat("lu",6)

result = Cat.oldest(cat1,cat2,cat3) 
print(f"The oldest cat is {result.name} , and is {result.age} years old")

#exercice 2
class Dog :
    def __init__(self,name,height):
        self.name = name
        self.height = height

    def bark (self):
        print(f"{self.name} goes woof!")    

    def jump (self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high! ")


davids_dog = Dog("rex",50)
print (davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()
print("---------------------------")
sarahs_dog = Dog("Teacup", 20)
print (sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print(sarahs_dog.name)
else:
    print(davids_dog.name)

# exercice 3

class Song :
    lyrics = []
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
# Exercice 4
class zoo :
    def __init__(self , zoo_name):
        animals = []
        self.name = zoo_name
    def add_animals(self,new_animal):
            if new_animal not in self.animals:
                self.animals.apprend()
    def get_animals(self):
        print (self.animals)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
          for letter in self.animal:
              letter = self.animals[0]
              result = {}

              if letter not in result:
                result[letter] = self.animal
              elif isinstance(result[letter], str):
                result[letter] = [result[letter], self.animal]
              else:
                result[letter].append(self.animal)

          return result         
    def get_groups(self):
         groups = self.sort_animals()

         for letter, animals in groups.items():
             print(letter)    
             if isinstance(animals, str):
               print(animals)
             else:
              for animal in animals:
                print(animal)
      
new_york_zoo = zoo("New York Zoo")

new_york_zoo.add_animals("Bear")
new_york_zoo.add_animals("Ape")
new_york_zoo.add_animals("Baboon")
new_york_zoo.add_animals("Cat")


new_york_zoo.get_animals()

new_york_zoo.get_groups()

new_york_zoo.sell_animal("Bear")
new_york_zoo.get_animals()

new_york_zoo.get_groups()

