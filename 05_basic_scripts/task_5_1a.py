# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP_network = input("Enter IP network in format x.x.x.x/x: ")

template_net = ['Network:', 
                '{0:<10}{1:<10}{2:<10}{3:<10}', 
                '{0:>08b}  {1:>08b}  {2:>08b}  {3:>08b}']
template_mask1 = ['Mask:', '/{4}']
template_mask2 = ['{:<10}{:<10}{:<10}{:<10}']

net_and_mask = [int(x) for x in IP_network.replace('/', '.').split('.')]
net_and_mask = [net_and_mask[4-i] for i in range(int((32 - net_and_mask[-1])/8))]
mask_bin = [('1' * net_and_mask[-1] + '0' * (32 - net_and_mask[-1]))
           [0 + i:8 + i] for i in range(0, 25, 8)]
mask_dec = [int(x, 2) for x in mask_bin]

print ('\n')
print ('\n'.join(template_net).format(*net_and_mask))
print ('\n'.join(template_mask1).format(*net_and_mask))
print ('\n')
print (template_mask2.format(*mask_dec))
print (template_mask2.format(*mask_bin))
