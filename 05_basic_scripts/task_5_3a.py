# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

interface = dict(access=[access_template, 'Enter VLAN number:'], 
                 trunk=[trunk_template, 'Enter allowed VLANs:'])
mode_if = input('Enter interface mode (access/trunk): ')
type_if = input('Enter interface type and number: ')
vlan_if = input(interface[mode_if][1])

print('\n' + 'interface ' + type_if)
print('\n'.join(interface[mode_if][0]).format(vlan_if))
