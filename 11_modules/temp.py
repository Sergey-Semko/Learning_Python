def parse_cdp_neighbors (input):
    commands = input.split('\n')
    dict = {}
    for command in commands:
        if command.startswith(' ') or command == '':
            pass
        elif 'show cdp neighbors' in command:
            l_name = command.split('>')[0]
        else:
            r_name, l_intf, l_port, h_time, *other, r_intf, r_port = command.split()
            if h_time[0].isdigit():
                dict[(l_name, l_intf + l_port)] = (r_name, r_intf + r_port)
                print(l_name, l_intf, l_port, r_name, r_intf, r_port)
    return dict

if __name__ == "__main__":
    f = open('sw1_sh_cdp_neighbors.txt')
    parse_com = parse_cdp_neighbors(f.read())
    f.close()

    print(parse_com)
