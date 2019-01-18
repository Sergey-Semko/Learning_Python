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

route_template = (
  'Protocol:              OSPF\n'
  'Prefix:                {1}\n'
  'AD/Metric:             {2}\n'
  'Next-Hop:              {4}\n'
  'Last update:           {5}\n'
  'Outbound Interface:    {6}'
)

for line in file:
    print(route_template.format(*line.replace('[', '').replace(']', '').replace(',', '').split()))
    print('-' * 40 + '\n')
file.close()
