"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

random_list = (1,2,3,"a","b","c",{1:"ee"},[1,2])
for i in range(len(random_list)):
    print(type(random_list[i]))

Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
"""
user_list = list((input("Ведите несколько значений: ")))

a_result = []

b_turn = False
if len(user_list)%2!=0:
    user_list.append(user_list[-1])
    b_turn = True

i=0
while i < len(user_list):
    a_result.append(user_list[i + 1])
    a_result.append(user_list[i])
    i = i + 2

if b_turn:
    a_result.pop()

user_list = a_result

print(user_list)