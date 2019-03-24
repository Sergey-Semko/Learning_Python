# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def parse_cdp_neighbors (input):
    commands = input.split('\n')
    dict = {}
    for command in commands:
        if command.startswith(' ') or command == '':
            pass
        elif 'show cdp neighbors' in command:
            l_name = command.split('>')[0]
        else:
            r_name, l_intf, l_port, h_time, *other, r_intf, r_port = command.split()
            if h_time[0].isdigit():
                dict[(l_name, l_intf + l_port)] = (r_name, r_intf + r_port)
    return dict

if __name__ == "__main__":
    f = open('sw1_sh_cdp_neighbors.txt')
    parse_com = parse_cdp_neighbors(f.read())
    f.close()

    print(parse_com)
