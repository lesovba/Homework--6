# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше 
# заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

min, max = int(input('Введите минимум диапазона: ')), int(input('Введите максимум диапазона: '))
list_1 = [1, 2, 4, 5, 6, 7, 8, 11]

def createList(minValue, maxValue, list_new):
    list_indexes = list()
    for i in range (1, len(list_1)):
        if list_new[i]>minValue and list_new[i]<maxValue:
           list_indexes.append(i)
    return list_indexes

print(list_1)
print(createList(min, max, list_1))