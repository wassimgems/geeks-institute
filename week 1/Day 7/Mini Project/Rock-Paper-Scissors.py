
from game import Game


def get_user_menu_choice():
    print("\n--- Menu ---")
    print("(g) Play a new game")
    print("(s) Show scores")
    print("(x) Quit")
    choice = input("Choose an option: ").lower()
    while choice not in ["g", "s", "x"]:
        print("Invalid choice. Please try again.")
        choice = input("Choose (g), (s), or (x): ").lower()
    return choice
def print_results(results):
    print("\n--- Game Results ---")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing!")
def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        answer_user = get_user_menu_choice()
        if answer_user == "g":
            game = Game()
            result = game.play()
            results[result] += 1
        elif answer_user == "s":
            print_results(results)

        elif answer_user == "x":
            print_results(results)
            break
if __name__ == "__main__":
    main()
