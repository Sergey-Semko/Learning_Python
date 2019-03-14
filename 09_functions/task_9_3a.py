# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(conf_file):
    access_dict = {}
    trunk_dict = {}
    with open(conf_file) as f:
        for line in f:
            if 'interface' in line:
                interface = line.split()[-1]
            elif 'mode access' in line:
                access_dict[interface] = 1
            elif 'access vlan' in line:
                vlan = int(line.split()[-1])
                access_dict[interface] = vlan
            elif 'trunk allowed vlan' in line:
                vlans = [int(item) for item in line.split()[-1].split(',')]
                trunk_dict[interface] = vlans
    return access_dict, trunk_dict

access_d, trunk_d = get_int_vlan_map('config_sw2.txt')

print(access_d)
print(trunk_d)
