#Daily challenge

import re
import operator

class Text:
    def __init__(self, text):
        self.text = text
        self.comma_sen = [] 
        self.count_words = {}
    def frequency(self):
        self.comma_sen = re.split('\W', self.text) #метод с использованием импорта модуля регулярных выраж,  делит на слова по пробелам и знакам, но может оставить пустые места
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
        
text = Text("A good book would sometimes cost as much as a good house.")
            
print(text.frequency()) #Смотрим как часто встречается слово
print(text.most_common())
print(text.unique_words())
        