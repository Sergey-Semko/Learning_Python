# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#solution

IP_network = input("Enter IP network in format x.x.x.x/x: ")

template_net = ['Network:', 
                '{0:<10}{1:<10}{2:<10}{3:<10}', 
                '{0:>08b}  {1:>08b}  {2:>08b}  {3:>08b}']
template_mask1 = ['Mask:', '/{4}']
template_mask2 = ['{:<10}{:<10}{:<10}{:<10}']

net_and_mask = [int(x) for x in IP_network.replace('/', '.').split('.')]
mask_bin = [
  ('1'*net_and_mask[-1] + '0' * (32-net_and_mask[-1]))[0+i : 8+i] for i in range(0, 25, 8)
]
mask_dec = [int(x, 2) for x in mask_bin]

print ('\n')
print ('\n'.join(template_net).format(*net_and_mask))
print ('\n'.join(template_mask).format(*net_and_mask))
print ('\n')
print (template_mask2.format(*mask_dec))
print (template_mask2.format(*mask_bin))
