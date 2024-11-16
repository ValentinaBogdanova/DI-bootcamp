from game import Game

def get_user_menu_choice():
     print("Menu:")
     print("1. Play a new game")
     print("2. Show scores")
     print("3. Quit")
     
     while True:
          try:
            user_menu_imput = int((input("Write a number: ")).strip())   # адаптируем
            if user_menu_imput == 1:
                return "Play"
            elif user_menu_imput == 2:
                return "Show scores"
            elif user_menu_imput == 3:
                return "Quit"
            else:
                print("Invalid imput. Try again")
          except ValueError:
           print("Invalid input. Please enter a valid number.")
            
# get_user_menu_choice()

def print_results(results):   #чисто показать результаты
    print("\nGame results:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")

def main():
    print("Welcome to Rock, Paper, Scissors! \n Get ready to test your luck and strategy against the computer. \nYou can play as many games as you want, check your scores, or exit anytime. \n Let's see if you've got what it takes to beat the computer! \nChoose an option from the menu below to get started!")
    playng_game = Game()  # Создаём объект игры
    while True:
        menu = get_user_menu_choice()
        if menu == "Play":
            playng_game.play()
        elif menu == "Show scores":
            print_results(playng_game.game_score)
        else:
            print()
            print("Exiting the game!")
            print_results(playng_game.game_score)
            break
if __name__ == "__main__":
    main()
