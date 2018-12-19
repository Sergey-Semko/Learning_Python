#!/usr/bin/env python3

from sys import argv

# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP_network = str(argv[1:])

#IP_network = input("Enter IP network in format x.x.x.x/x: ")

template_net = ['Network:', 
                '{0:<10}{1:<10}{2:<10}{3:<10}', 
                '{0:>08b}  {1:>08b}  {2:>08b}  {3:>08b}']
template_mask1 = ['Mask:', '/{4}']
template_mask2 = '{:<10}{:<10}{:<10}{:<10}'

net_and_mask = [int(x) for x in IP_network.replace('/', '.').split('.')]
mask_bin = [
  ('1'*net_and_mask[-1] + '0' * (32-net_and_mask[-1]))[0+i : 8+i] for i in range(0, 25, 8)
]
mask_dec = [int(x, 2) for x in mask_bin]

print ('\n')
print ('\n'.join(template_net).format(*net_and_mask))
print ('\n')
print ('\n'.join(template_mask1).format(*net_and_mask))
print (template_mask2.format(*mask_dec))
print (template_mask2.format(*mask_bin))
