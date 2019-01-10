# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Solution 1
'''
try:
    IP_address = [int(x) for x in input("Enter IP address in format 10.0.1.1: ").split('.')]
    for i in range(4):
        if IP_address[i] not in range(0, 256):
            print('Incorrect IPv4 address')
            exit()
except (ValueError, IndexError):
    print('Incorrect IPv4 address')
else:
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
'''
#Solution 2
IP_address = input("Enter IP address in format 10.0.1.1: ")		
if IP_addrss.count('.') == 3:
    IP_address = [int(x) for x in IP_address.split('.')]
    for part in IP_address:
        if part not in range(0,256):
            print('Incorrect IPv4 address')
            exit()
else:
    print('Incorrect IPv4 address')
    exit()

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
