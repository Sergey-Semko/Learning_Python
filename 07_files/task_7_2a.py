# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
ignore_presence = False

file_name = argv[1]
file = open(file_name, 'r')

for line in file:
    if not line.startswith('!'):
        for word in ignore:
            if line.find(word) > -1:
                ignore_presence = True
                break
        if not ignore_presence:
            print (line.strip())
        else:
            ignore_presence = False
file.close()
