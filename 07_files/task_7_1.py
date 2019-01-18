# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
file = open('ospf.txt', 'r')

route_template = "Protocol:              OSPF\nPrefix:                {1}\nAD/Metric:             {2}\nNext-Hop:              {4}\nLast update:           {5}\nOutbound Interface:    {6}"

for line in file:
    print(route_template.format(*line.replace('[', '').replace(']', '').replace(',', '').split()))
    print('-' * 40 + '\n')
file.close()
