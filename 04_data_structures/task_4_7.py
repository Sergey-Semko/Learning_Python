# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'

#Solution
MAC_list = MAC.split(":") 

MAC_list 
#['AAAA', 'BBBB', 'CCCC']

#[int(x,16) for x in MAC_list] 
#[43690, 48059, 52428]

#[bin(int(x,16)) for x in MAC_list] 
#['0b1010101010101010', '0b1011101110111011', '0b1100110011001100']

MAC_list_dec = [int(x,16) for x in MAC_list] 
MAC_list_dec 
#[43690, 48059, 52428]

print('{0[0]:08b} {0[1]:08b} {0[2]:08b}'.format(MAC_list_dec)) 
#1010101010101010 1011101110111011 1100110011001100

#Variant2
print('{:08b} {:08b} {:08b}'.format(*MAC_list_dec))
