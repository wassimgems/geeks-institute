

# challenge 1

number = int(input("enter a number:"))
lenght = int(input("enter the length:"))


multiples = []
for i in range(1, lenght +1):
    multiples.append(number * i)


print(multiples)

# challenge 2


user_word = input("enter a word: ")
new_word = ""
for i in range(len(user_word)):
    if user_word[i] != user_word[i-1] or i == 0:
        new_word += user_word[i]
 
print(new_word)
