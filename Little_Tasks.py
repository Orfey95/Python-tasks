def task_1_1():
    NAT = "ip nat inside source list ACL interface FastEthernet0/1 over"
    NAT = NAT.replace("FastEthernet", "GigabitEthernet")
    return NAT


def task_1_2():
    mac = 'AAAA:BBBB:CCCC'
    mac = mac.replace(":", ".")
    return mac


def task_1_3():
    config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
    config = config.split(" ")
    config = config[len(config) - 1].split(",")
    return config


def task_1_4():
    vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    valans = list(sorted(set(vlans)))
    return valans


def task_1_5():
    command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
    command2 = 'switchport trunk allowed vlan 1,3,8,9'
    command1 = command1.split(" ")
    command1 = command1[len(command1) - 1].split(",")
    command2 = command2.split(" ")
    command2 = command2[len(command2) - 1].split(",")
    command_result = sorted(list(set(command1) & set(command2)))
    return command_result


def task_1_6():
    ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
    protocol = ospf_route.split(" ")[0]
    print("%-20s %s" % ("Protocol: ", protocol))
    prefix = ospf_route.split(" ")[1]
    print("%-20s %s" % ("Prefix: ", prefix))
    AD_metric = (ospf_route.split(" ")[2])[1:-1]
    print("%-20s %s" % ("AD/Metric: ", AD_metric))
    next_hop = (ospf_route.split(" ")[4])[:-1]
    print("%-20s %s" % ("Next-Hop: ", next_hop))
    last_update = (ospf_route.split(" ")[5])[:-1]
    print("%-20s %s" % ("Last update: ", last_update))
    outbound_interface = (ospf_route.split(" ")[6])
    print("%-20s %s" % ("Outbound Interface: ", outbound_interface))


def task_1_7():
    mac = 'AAAA:BBBB:CCCC'
    mac = mac.replace('A', '1010')
    mac = mac.replace('B', '1011')
    mac = mac.replace('C', '1100')
    mac = mac.replace(':', '')
    return mac


def task_1_8():
    ip = '192.168.3.1'
    binary_ip = []
    decimal_ip = ip.split('.')
    for x in range(len(decimal_ip)):
        binary_ip.append((bin(int(decimal_ip[x]))[2:]).zfill(8))
    print("%-10s %-10s %-10s %s" % (decimal_ip[0], decimal_ip[1], decimal_ip[2], decimal_ip[3]))
    print("%-10s %-10s %-10s %s" % (binary_ip[0], binary_ip[1], binary_ip[2], binary_ip[3]))
