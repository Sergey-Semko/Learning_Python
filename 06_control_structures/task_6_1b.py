# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Solution
address_correct = False
while not address_correct:
    IP_address = input("Enter IP address in format 10.0.1.1: ")
    if IP_address.count('.') == 3:
        IP_address = [x for x in IP_address.split('.')]
        for part in IP_address:
            if part.isdigit():
                part = int(part)
                if part in range(0,256):
                    address_correct = True
                else:
                    address_correct = False
                    print('Incorrect IPv4 address')
                    break
            else:
                address_correct = False
                print('Incorrect IPv4 address')
                break
    else:
        print('Incorrect IPv4 address')

if (
  IP_address[0] in range(1, 128)
  or IP_address[0] in range(127, 192)
  or IP_address[0] in range (191, 224)
):
    print('unicast')
elif IP_address[0] in range(223, 240):
    print('multicast')
elif (
  IP_address[0]==255
  and IP_address[1]==255
  and IP_address[2]==255
  and IP_address[3]==255
):
    print('local broadcast')
elif (
  IP_address[0]==0
  and IP_address[1]==0
  and IP_address[2]==0
  and IP_address[3]==0
):
    print('unassigned')
else:
    print('unused')
