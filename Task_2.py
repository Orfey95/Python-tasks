import re


def task_2_1():
    mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
    mac_cisco = []
    for x in range(len(mac)):
        mac_cisco.append(mac[x].replace(":", "."))
    return mac_cisco


def task_2_2():
    print("Input ip address (example: 192.168.0.1):")
    ip_address = input()
    split_ip_address = re.split(r'\.', ip_address)
    if 1 <= int(split_ip_address[0]) <= 223:
        print("unicast")
    else:
        if 224 <= int(split_ip_address[0]) <= 239:
            print("multicast")
        else:
            if split_ip_address[0] and \
                    split_ip_address[1] and \
                    split_ip_address[2] and \
                    split_ip_address[3] == '255':
                print("local broadcast")
            else:
                if split_ip_address[0] and \
                        split_ip_address[1] and \
                        split_ip_address[2] and \
                        split_ip_address[3] == '0':
                    print("unassigned")
                else:
                    print("unused")


def task_2_3():
    print("Input ip address (example: 192.168.0.1):")
    ip_address = input()
    if not re.match(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])', ip_address):
        return "Invalid IP Address"
    split_ip_address = re.split(r'\.', ip_address)
    if 1 <= int(split_ip_address[0]) <= 223:
        print("unicast")
    else:
        if 224 <= int(split_ip_address[0]) <= 239:
            print("multicast")
        else:
            if split_ip_address[0] and \
                    split_ip_address[1] and \
                    split_ip_address[2] and \
                    split_ip_address[3] == '255':
                print("local broadcast")
            else:
                if split_ip_address[0] and \
                        split_ip_address[1] and \
                        split_ip_address[2] and \
                        split_ip_address[3] == '0':
                    print("unassigned")
                else:
                    print("unused")


def task_2_4():
    print("Input ip address (example: 192.168.0.1):")
    while True:
        ip_address = input()
        if not re.match(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])', ip_address):
            print("Invalid IP Address. Input again.")
        else:
            break
    split_ip_address = re.split(r'\.', ip_address)
    if 1 <= int(split_ip_address[0]) <= 223:
        print("unicast")
    else:
        if 224 <= int(split_ip_address[0]) <= 239:
            print("multicast")
        else:
            if split_ip_address[0] and \
                    split_ip_address[1] and \
                    split_ip_address[2] and \
                    split_ip_address[3] == '255':
                print("local broadcast")
            else:
                if split_ip_address[0] and \
                        split_ip_address[1] and \
                        split_ip_address[2] and \
                        split_ip_address[3] == '0':
                    print("unassigned")
                else:
                    print("unused")


def task_2_5():
    trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk allowed vlan'
    ]
    trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }
    for intf, vlan in trunk.items():
        print('interface FastEthernet' + intf)
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                first = vlan.pop(0)
                if first == 'add':
                    print(' ' + command + ' ' + first + ' ' + ','.join(map(str, vlan)))
                if first == 'del':
                    print(' ' + command + ' ' + 'remove' + ' ' + ','.join(map(str, vlan)))
                if first == 'only':
                    print(' ' + command + ' ' + ','.join(map(str, vlan)))
            else:
                print(' {}'.format(command))


print(task_2_5())
