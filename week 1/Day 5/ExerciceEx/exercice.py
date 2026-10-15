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


