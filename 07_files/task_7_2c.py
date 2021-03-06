# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
ignore_presence = False

file_name_in, file_name_out = argv[1:]

file_in = open(file_name_in, 'r')
file_out = open(file_name_out, 'w')

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
