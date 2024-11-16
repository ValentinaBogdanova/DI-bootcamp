class AnagramChecker:
    def __init__(self, anagrams): #инициализируем класс 
        self.anagrams = anagrams
    def is_valid_word(self,user_word):   #проверяю есть ли слово в списке, то есть является ли анограмой
        user_word = str(user_word).upper()
        if user_word in self.anagrams:   
            return True
        else:
            return False
    def get_anagrams(self,user_word):  #получаем ананограмы
        user_word = str(user_word)
        found_anagrams = []
        for word in self.anagrams:
            if sorted(word.upper()) == sorted(user_word.upper()) and word != user_word.upper(): #убираем слово введенное из списка
                found_anagrams.append(word)
        return found_anagrams
    

with open("C:/Users/Acer/Desktop/DI-bootcamp/Week2/Day5/sowpods.txt", "r", encoding = "utf-8") as file:
    anagrams = file.readlines() #преобразуем строки в список
    anagrams = [word.strip() for word in anagrams] #убираем лишние пробелы
        
# print(anagrams)


instruction = "This program checks if a word is a valid anagram and displays a list of words that are its anagrams.\n Please enter only a single word, without any numbers or special characters."

def user_interface():
    checker = AnagramChecker(anagrams) 
    print(instruction)
    while True:
        try:
            user_input = input("To enter a word, type 1. To exit the program, type 2.")
            if not user_input.isdigit(): #проверяем число ли 
                raise ValueError # исключаем если ввод не число
            repited_ask = int(user_input) # в любом случае делаем интеджер 
            if repited_ask == 1:
                    user_word = input("Write a word:  ").strip()  #просим ввести слово
                    if user_word.isalpha(): #проверяем буквы ли
                        if checker.is_valid_word(user_word): #проверяем через созданный класс
                            result = checker.get_anagrams(user_word)
                            if result:
                                string_anagrams = ", ".join(result)
                                print(f"YOUR WORD: {user_word}")
                                print("this is a valid English word.")
                                print(f'Anagrams for {user_word}: {string_anagrams}')
                            else:
                                print(f"No anagrams found for {user_word}.")
                        else:
                            print("No anagrams found for the given word.")
                    else:
                        print("Invalid input")
            elif repited_ask == 2:
                print("You have exited the program. Come back anytime if you need anagrams.")
                break
            else:
                print("Invalid choice. Please enter 1 to continue or 2 to exit.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
user_interface()