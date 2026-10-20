import random


class Game:
    def __init__(self):
        pass
    def get_user_item(self):
        res = ""
        while res not in ["r", "p", "s"]:
            res = input("Choose (r)ock, (p)aper or (s)cissors:")
            if res not in  ["r", "p", "s"]:
                print ("Invalid choice. Try again.")
            else:
                return res 
        
    def get_computer_item(self):
        random_liste = ["r", "p", "s"]
        return random.choice(random_liste)

    def get_game_result(self, user_item, computer_item):
        
        if user_item == computer_item:
            return "draw"
        elif user_item == "r" and computer_item =="p":
            return "lose"
        elif user_item == "r" and computer_item =="s":
            return "won"
        elif user_item == "p" and computer_item =="r":
            return "won"
        elif user_item == "p" and computer_item =="s":
            return "lose"
        elif user_item == "s" and computer_item =="p":
            return"won"
        elif user_item == "r" and computer_item =="p":
            return"lose"
    
    def play(self):
       user_items = self.get_user_item()
       computer_item = self.get_computer_item()
       result = self.get_game_result(user_items, computer_item)
       print(f" you selcted {user_items}")
       print(f" The computer selected {computer_item}")
       print(f" you {result}!")
       return result