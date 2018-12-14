# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается 
с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны 
и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. 
А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]
print('num_list: ' + str(num_list))
print('word_list: ' + str(word_list) + '\n')
num_el = int(input('Enter the element from list num_list: '))
word_el = input('Enter the element from list word_list: ')
print(
    'The last index of ' + num_el + ' in num_list is: ' 
      + str(len(num_list) - 1 - num_list[::-1].index(num_el))
)
print(
    'The last index of ' + word_el + ' in num_list is: ' 
      + str(len(word_list) - 1 - word_list[::-1].index(word_el))
)
