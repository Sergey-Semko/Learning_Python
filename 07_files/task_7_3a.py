# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
file = open('CAM_table.txt', 'r')

vlans_list = []
for line in file:
    if line.count('.') == 2:
        vlans_list.append(line.strip())
vlans_list.sort()
for item in vlans_list:
    print(' {0:8}{1:17}{3}'.format(*item.split()))
file.close()
