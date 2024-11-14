#Daily challenge

import re
import operator
import string
from nltk.corpus import stopwords

class Text:
    def __init__(self, text):
        self.text = text
        self.comma_sen = [] 
        self.count_words = {}
    def frequency(self):
        self.comma_sen = re.split('\\W', self.text) #метод с использованием импорта модуля регулярных выраж,  делит на слова по пробелам и знакам, но может оставить пустые места
        self.comma_sen = [word.lower() for word in self.comma_sen if word] #убираю пустые места list comprehension 
        self.count_words = {}
        for element in self.comma_sen:
            if element in self.count_words: #метод гет для доставать по ключу значения
                self.count_words[element] += 1  
            else:
                self.count_words[element] = 1
        sorted_words = sorted(self.count_words.items(), key=operator.itemgetter(1), reverse=True)  #делает картеж, потом указывает что ключ к сортировки это второй элемент (частота встрч), true  так как по убыванию
        return sorted_words  #важно было создать отдельную переменную а не перезописывать словарь (в таком случае он меняет его на список)
    def most_common(self):
        sorted_words = self.frequency()
        if sorted_words:
            return sorted_words[0]
        else:
            return None
    def unique_words(self):
        return  [word for word, count in self.count_words.items() if count == 1]   #собирает список из слов-ключей если в словаре значение было 1
    
    @classmethod #делаю класс метод так как он прозволяет обращаться напрямую к классу и создавать новые объекты
    
    def from_file(cls, filename):
        with open(filename , "r", encoding="utf-8") as file:
            text = file.read()
            return cls (text)

stranger_text= Text.from_file("C:\\Users\\Acer\\Desktop\\DI-bootcamp\\Week2\\Day4\\the_stranger.txt")
# print(stranger_text.text)

# print(stranger_text.frequency())
# print(stranger_text.most_common())
# print(stranger_text.unique_words())
        
# text = Text("A good book would sometimes cost as much as a good house.")
            
# print(text.frequency()) #Смотрим как часто встречается слово
# print(text.most_common())
# print(text.unique_words())

class TextModification(Text):
    def remove_punct(self):
        self.text = self.text.translate(str.maketrans('', '', string.punctuation))
        return self.text 
    def remove_stop_words(self):
        stop_words = set(stopwords.words('english')) # Удаляем английские стоп-слова из текста  это распространённые слова, которые часто встречаются в тексте, но обычно не несут значимой информации для анализа
        words = self.text.split()  
        self.text = ' '.join([word for word in words if word.lower() not in stop_words])
        return self.text 
    def remove_special_characters(self):
        self.text = re.sub(r'[^A-Za-z0-9\s]', '', self.text) # Удаляет специальные символы из текста
        return self.text 

stranger_text = TextModification.from_file("C:\\Users\\Acer\\Desktop\\DI-bootcamp\\Week2\\Day4\\the_stranger.txt") #вызаем файл с помощью подкласса

# print(stranger_text.remove_punct())
# print(stranger_text.remove_stop_words())
# print(stranger_text.remove_special_characters())