# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# Solution
IP_address = input("Enter IP address in format 10.0.1.1: ")
IP_address = [int(x) for x in IP_address.split('.')]

if (IP_address[0]>0 and IP_address[0]<=127) or
   (IP_address[0]>127 and IP_address[0]<=191) or
   (IP_address[0]>191 and IP_address[0]<=223):
   print('unicast')
elif IP_address[0]>223 and IP_address[0]<=239:
   print('multicast')
elif IP_address[0]==255 and
   IP_address[1]==255 and
   IP_address[2]==255 and
   IP_address[3]==255:
   print('local broadcast')
elif IP_address[0]==0 and
   IP_address[1]==0 and
   IP_address[2]==0 and
   IP_address[3]==0:
   print('unassigned')
else:
   print('unused')
