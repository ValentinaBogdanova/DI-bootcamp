# #DATE STRUCTURES:


# #sequences = string (последовательность)
# #data structure sequences = list
# #sets (множество)
# #tuples (кортеж ,запись)

# my_name="Valentina"
# last_name="Bogdanova"
# user_name="vb19"

# user_info  = [my_name,last_name,user_name] #так выглядит лист со сбором переменных
# #прямы скобки и кома (запятая)

# user_information=list(my_name)
# print(user_info)
# print(user_information) # разбивает строку на список 

# option1=["Valentina"]
# option2=list('Valentita')
# print(option1)
# print(option2)

# nums_list=[1,2,4,5,6,7,8,]  #в list можно добавлять любые переменные
# #они могут быть разного типа

#___________________________________________

# #LIST METHODS

# .APPEND
# # nums_list.append(291) # добавляет в конец списка
# # print(nums_list)

# .INSERT
# # nums_list.insert(2,55) # 2- это индекс (начинается с 0),  55 - элемент
# # print(nums_list)


# .REMOVE
# # nums_list.remove(2) #убирает только первое проявление переменной в списке
# # print(nums_list)


# DEL ____
# # del nums_list[3] #убирает переменную по индексу (локации)
# # print(nums_list) 

# .POP
# # nums_list.pop() #убирает последнее
# # print(nums_list)
# # nums_list.pop(3) # убирает по индексу
# # print(nums_list)
# # deleted_el=nums_list.pop(3)  # создаем новую переменную для убранного элемента из списка
# # print(deleted_el) # так мы можем посмотреть что удалили

# using .INDEX
# # print(nums_list.index(2))
# # nums_list[2]=40  #заменить по индексу в списке
# # print(nums_list)


# # #list indexing
# # print(nums_list[3:])
# # print(nums_list[3])


#_______________________________

# # #TUPLE is fixed (unmuted) list мы не можем менять последовательность 
# # some_tuple=tuple()
# # my_tuple=(10,5,9,86,56)
# # scores=(10,15,76,34)
# # scores_list=list(scores) # Делаем список из кортежа
# # scores_list.append(20) # добавляем в лист что нужно
# # # обновляем кортеж
# # update_tuble=tuple(scores_list)

# # #unpack tuple
# # score1, score2, score3, score4 = scores
# # print(score1)
# # print(score2)
# # print(score3)
# # # List это хранение переменных
# # print(type(update_tuble)) #всомнить какой тип переменной


# # list1=[5,10,15,20,25,50,20]
# # if list1.index(20):  #узнаем есть ли это число и его индекс
# #     list1[list1.index(20)]=200 #заменяем по индексу
# # print(list1)


#____________________________________

# # # SET МНОЖЕСТВА!!!


# # my_set={}
# # my_set=set()

# # my_set.add("Rick")
# # my_set.add('Morty')
# # my_set.add('Rick')

# # print(my_set)
# # #print(my_set[0])  - НЕВОЗМОЖНО ОПРЕДЕЛИТЬ ИНДЕКС В множестве


# # set2={'Harry', "Ron", "Morty"}
# # set3=my_set.intersection(set2) #где пересекаются два сета 
# # print(set3)

# # set4 = my_set.union(set2) #объединяет два множества
# # print(set4)

# SET DOEST ALLOW ПОВТОРЕНИЯ
# чуыствителен к регистру А и а - определяет как разное 

# чтобы удалить дубликаты в листе , делаем множество из листа а затем создаем новый лит
# таким образм все дубликаты будут удалены

# names=["Lean","Luke","Ron","Harry","Harry"]
# names_set=set(names) #создаем множество (оно всегда перемешано)
# names_updated=list(names_set) 
# print(names_updated)

#_______________________________

# LOOPS позволяет повторять действие поочередно с каждой переменной в последовательности 
#syntax

# students=["Alex", "Noah", "Sara", "Dima"]
# for each_sudent in students:  # for ____ in делает действие с каэдой переменной в листе 
#    if each_sudent=="Dima":
#     print(f'Dobroe Utro, {each_sudent}')
#    else:    
#     print(f"Welcome, {each_sudent}")


# for i in range(1,10): # это диапазон он ДО 10 (не включая 10)
#   print(f"Hello there {i}") # пишет номер операциии (так как это диапазон)

# for i in range(len(students)): # внутрь range все что считается числом
#   print(f"Hello there {i}") # лучше использовать len 


#   # FOR___IN где одно 

#   for i, each_sudent in enumerate(students): #перечисление
#     print(i, each_sudent)

# my_nums=[3,6,8,9,47,54] #MIN MAX SUM (use for ___in behide the scene)
# print(sum(my_nums))

# output=0
# for i in range(len(my_nums)): 
#  output += my_nums[i]
#  print(output)



 # WHITE LOOP  ВСЕГДА НАДО  УКАЗЫВАТЬ ГДЕ ОСТАНОВИТЬСЯ
#  i=0
#  while i<10:
#    print(f"hi {i}") #БЕСКОНЕЧНО



#ТУТ Я НЕ ПОНЯЛА

# family=[]
# keep_asking = True # лучше писать переменную до LOOP
# members=input('write family member name. press "q" to finish')
# while keep_asking:
#    members=input('write family member name. press "q" to finish')
#    if members =="q": 
#      keep_asking = False 
# family.append(members)
#         print(family)

# print("Final family list:", family)