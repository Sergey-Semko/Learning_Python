# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
ignore_presence = False

file_name = argv[1]
file_in = open(file_name, 'r')
file_out = open('config_sw1_cleared.txt', 'w')

for line in file_in:
    for word in ignore:
        if line.find(word) > -1:
            ignore_presence = True
            break
    if not ignore_presence:
        file_out.write(line)
    else:
        ignore_presence = False
file_in.close()
file_out.close()
