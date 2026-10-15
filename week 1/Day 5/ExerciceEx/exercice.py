
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