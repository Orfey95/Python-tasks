import math
import re


def get_sub_networks():
    print("Input ip address with subnet mask (example: 146.132.126.0/22):")
    default_ip_and_mask = input()
    if default_ip_and_mask == '':
        default_ip_and_mask = '146.132.126.0/22'
    if not re.match(r'^(\d{1,3}\.){3}\d{1,3}/\d+$', default_ip_and_mask):
        return "IP address or subnet mask is not correct, example: 146.132.126.0/22"

    # split input into ip address and subnet mask
    split_ip_and_mask = re.split(r'/', default_ip_and_mask)
    ip_address = split_ip_and_mask[0]
    subnet_mask = split_ip_and_mask[1]
    if int(subnet_mask) > 32:
        return "Subnet mask cannot be more than 32"

    # variables declaration
    binary_ip_address = ''
    decimal_network_ip_address = ''

    # split ip address into octets
    split_ip_address = re.split(r'\.', ip_address)

    # calculate binary ip address
    for x in range(len(split_ip_address)):
        binary_ip_address += str(bin(int(split_ip_address[x]))[2:].zfill(8))

    # calculate network ip address
    binary_network_ip_address = binary_ip_address[:int(subnet_mask)]
    for x in range(32 - int(subnet_mask)):
        binary_network_ip_address += '0'
    split_binary_network_ip_address = re.findall('........', binary_network_ip_address)
    for x in range(4):
        decimal_network_ip_address += str(int(split_binary_network_ip_address[x], 2)) + '.'
    decimal_network_ip_address = decimal_network_ip_address[:-1]

    # getting network size
    print("Input number of hosts in network:")
    number_host = int(input()) + 2

    #  counting new mask
    new_mask = int(32 - math.ceil(math.log(int(number_host), 2)))

    # get sub networks
    temp_number_host = 0
    return_list = list()
    for x in range(2 ** (new_mask - int(subnet_mask))):
        return_list.append(f"{x+1} - {add_number_to_ip_address(decimal_network_ip_address, temp_number_host)}/{new_mask}")
        temp_number_host = temp_number_host + (2 ** (32 - new_mask))
    return "\n".join(return_list)


def add_number_to_ip_address(ip, add_number):
    # split ip address into octets
    split_ip_address = re.split(r'\.', ip)
    
    # add add_number to ip address
    split_ip_address[3] = int(split_ip_address[3]) + add_number
    for x in range(3, 0, -1):
        if (int(split_ip_address[x])) > 255:
            split_ip_address[x-1] = int(split_ip_address[x-1]) + (int(split_ip_address[x]) // 255)
            split_ip_address[x] = (int(split_ip_address[x])) % 255
    return '.'.join([str(elem) for elem in split_ip_address])


print(get_sub_networks())
