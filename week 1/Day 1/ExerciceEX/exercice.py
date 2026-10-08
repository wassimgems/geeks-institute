
# Exercise 1

print("Hello world  \n" * 4)


# Exercise 2

result = (99**3) * 8

print(result)

# Exercise 3

name = input ("what is your name ? ")
if name == 'wassim':
    print("we have the same name")

else:
    print ("we have different names")


    # Exercise 4 

height = int (input("what is your height ?"))

if height >145:
    print("you are tall enough to ride")

else:
    print("you are not tall enough to ride")

 # Exercise 5

my_fav_numbers = {8, 12, 16, 20, 24}
my_fav_numbers.add(5.7)
my_fav_numbers.pop()
friend_fav_numbers = {7, 8, 9, 10, 11}
our_fav_numbers = my_fav_numbers | friend_fav_numbers

# Exercise 6  

# no

# Exercise 7

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
len(basket)
basket.clear()
print(basket)

  #Exercise 8


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print("I made your {}".format(sandwich))