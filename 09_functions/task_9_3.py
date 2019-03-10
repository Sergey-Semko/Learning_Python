# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(conf_file):
    access_dict = {}
    trunk_dict = {}
    with open(conf_file) as f:
        for line in f:
            if 'interface' in line:
                interface = line.split()[-1]
            elif 'access vlan' in line:
                vlan = int(line.split()[-1])
                access_dict[interface] = vlan
            elif 'trunk allowed vlan' in line:
                vlans = line.split()[-1].split(',')
                trunk_dict[interface] = vlans
    return access_dict, trunk_dict

#access_d = {}
#trunk_d = {}
access_d, trunk_d = get_int_vlan_map('config_sw1.txt')

print(access_d)
print(trunk_d)
