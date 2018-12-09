# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
#Solution
ospf_route_list = ospf_route.replace('[', '').replace(']', '').replace(',', '').split()

#Variant1
route_template1=''' 
Protocol:               OSPF 
Prefix:                 {0[1]}
AD/Metric:              {0[2]}
Next-Hop:               {0[4]}
Last update:            {0[5]}
Outbound Interface:     {0[6]}
'''
print(route_template1.format(ospf_route_list))
#Protocol:               OSPF
#Prefix:                 10.0.24.0/24
#AD/Metric:              110/41
#Next-Hop:               10.0.13.3
#Last update:            3d18h
#Outbound Interface:     FastEthernet0/0

#Variant2
route_template2=''' 
Protocol:               OSPF 
Prefix:                 {1}
AD/Metric:              {2}
Next-Hop:               {4}
Last update:            {5}
Outbound Interface:     {6}
'''
print(route_template2.format(*ospf_route_list))
#Protocol:               OSPF
#Prefix:                 10.0.24.0/24
#AD/Metric:              110/41
#Next-Hop:               10.0.13.3
#Last update:            3d18h
#Outbound Interface:     FastEthernet0/0
