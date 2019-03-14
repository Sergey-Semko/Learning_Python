# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)

def config_to_dic(conf_file):
    result = {}
    with open(conf_file) as f:
        for line in f:
            if line.startswith('!') or check_ignore(line, ignore):
                continue
            elif not line.startswith(' '):
                main_command = line.strip()
                three_level = false
                result[main_command] = []
            elif line.startswith(' '):
                result[main_command].append(line.strip())
            elif line.startswith('  '):
                if not three_level:
                    last_command = result[main_command][-1]
                    result[main_command] = {key: {} for key in result[main_command]}
                    result[main_command][last_command] = []
                    three_level = true
                result[main_command][last_command].append(line.strip())
    return result

conf = config_to_dic('config_r1.txt')
print(conf)

