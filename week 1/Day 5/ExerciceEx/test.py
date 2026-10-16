class zoo :
    def __init__(self , zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animals(self,new_animal):
            if new_animal not in self.animals:
                self.animals.append(new_animal)
    def get_animals(self):
        print (self.animals)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
          for animal in self.animals:
              letter = self.animals[0]
              result = {}

              if letter not in result:
                result[letter] = self.animals
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

