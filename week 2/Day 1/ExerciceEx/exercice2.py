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

dog1 = Dog("Max", 5, 7)
print(dog1.bark())