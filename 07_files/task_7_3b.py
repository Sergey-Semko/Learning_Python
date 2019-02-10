# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
file = open('CAM_table.txt', 'r')

vlans_list = []
for line in file:
    if line.count('.') == 2:
        vlans_list.append(line.strip())
vlans_list.sort()
vlan = input ('Номер VLAN-a по которому необходима информация: ')
for item in vlans_list:
    if item.find(vlan) == 0
        print(' {0:8}{1:17}{3}'.format(*item.split()))
file.close()
