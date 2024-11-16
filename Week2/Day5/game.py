import random
class Game:
    def __init__(self):
        self.moves = ['r','p','s']                                                          # сохраняем возможные ходы: r - камень , s - ножницы, p - бумага
        self.game_score = {'win': 0, 'loss': 0, 'draw': 0}                                  # записываем сюда счет
    def get_user_item(self):
         print("Choose your move. If you pick Rock, type the letter 'R'.\n If you pick Paper, type the letter 'P'. If you pick Scissors, type the letter 'S'.")
         while True:                                                                        #чтобы циклился процес ожидания правильного вввода 
            user_choice = input("Enter your choice:   ").strip().lower()                    #убираем пробелы приводим к нижнему регистру
            if user_choice in self.moves:
                return user_choice                                                          #возвращаем ход пользователя
            else:
                print("Invalid input. You can only pick 'R'- rock, 'P' - paper or 'S' - scissors")
    def get_computer_item(self): 
        computer_choice = random.choice(self.moves)                                         #рандомный выбор из списка
        return computer_choice
    def get_game_result(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif user_choice == 'r' and computer_choice == 's':                                 #  if (user_choice, computer_choice) in [('r', 's'), ('p', 'r'), ('s', 'p')]:
            return "win"                                                                    #return "win"    можно так написать 
        elif user_choice == 'p' and computer_choice == 'r':
            return "win"
        elif user_choice == 's' and computer_choice == 'p':
            return "win"
        else:
            return "loss"
    def play(self):
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice,computer_choice)                          #сравниваем рез-ты
        self.game_score[result] += 1                                                                     #обновляем счет
        print(f"You chose {user_choice}. The computer chose {computer_choice}. Result: {result}.")
        #print(f'Current score - Wins: {self.game_score['win']}, Losses: {self.game_score['loss']}, Draws: {self.game_score['draw']}')  #показываем счет игры
        return result




# game = Game()
# print(game.get_computer_item())  #тест

