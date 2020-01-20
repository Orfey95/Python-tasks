import re


def check_ip4():
    print("Input ip address with subnet mask (example: 192.168.0.1/24):")
    default_ip_and_mask = input()
    if default_ip_and_mask == '':
        default_ip_and_mask = '192.168.0.1/24'
    if not re.match(r'^(\d{1,3}\.){3}\d{1,3}/\d+$', default_ip_and_mask):
        return "IP address or subnet mask is not correct, example: 192.168.0.1/24"
    # split input into ip address and subnet mask
    split_ip_and_mask = re.split(r'/', default_ip_and_mask)
    ip_address = split_ip_and_mask[0]
    subnet_mask = split_ip_and_mask[1]
    if int(subnet_mask) > 32:
        return "Subnet mask cannot be more than 32"
    # split ip address into octets
    split_ip_address = re.split(r'\.', ip_address)
    for x in range(4):
        if int(split_ip_address[x]) > 255:
            return "IP address octet cannot be more than 255"
    # variables declaration
    binary_ip_address = ''
    binary_subnet_mask = ''
    decimal_subnet_mask = ''
    decimal_broadcast_ip_address = ''
    decimal_network_ip_address = ''
    decimal_host_min_ip_address = ''
    decimal_host_max_ip_address = ''
    decimal_host_number_ip_address = ''
    # calculate binary ip address
    for x in range(len(split_ip_address)):
        binary_ip_address += str(bin(int(split_ip_address[x]))[2:].zfill(8))
    # calculate subnet mask
    for x in range(int(subnet_mask)):
        binary_subnet_mask += '1'
    full_binary_subnet_mask = ''.join(reversed(binary_subnet_mask.zfill(32)))
    split_full_binary_subnet_mask = re.findall('........', full_binary_subnet_mask)
    for x in range(4):
        decimal_subnet_mask += str(int(split_full_binary_subnet_mask[x], 2)) + '.'
    decimal_subnet_mask = decimal_subnet_mask[:-1]
    # calculate network size
    network_size = 2 ** (32 - int(subnet_mask))
    # calculate broadcast ip address
    binary_broadcast_ip_address = binary_ip_address[:int(subnet_mask)]
    for x in range(32 - int(subnet_mask)):
        binary_broadcast_ip_address += '1'
    split_binary_broadcast_ip_address = re.findall('........', binary_broadcast_ip_address)
    for x in range(4):
        decimal_broadcast_ip_address += str(int(split_binary_broadcast_ip_address[x], 2)) + '.'
    decimal_broadcast_ip_address = decimal_broadcast_ip_address[:-1]
    # calculate network ip address
    binary_network_ip_address = binary_ip_address[:int(subnet_mask)]
    for x in range(32 - int(subnet_mask)):
        binary_network_ip_address += '0'
    split_binary_network_ip_address = re.findall('........', binary_network_ip_address)
    for x in range(4):
        decimal_network_ip_address += str(int(split_binary_network_ip_address[x], 2)) + '.'
    decimal_network_ip_address = decimal_network_ip_address[:-1]
    # calculate host minimal ip address
    binary_host_min_ip_address = binary_network_ip_address[:-1] + '1'
    split_binary_host_min_ip_address = re.findall('........', binary_host_min_ip_address)
    for x in range(4):
        decimal_host_min_ip_address += str(int(split_binary_host_min_ip_address[x], 2)) + '.'
    decimal_host_min_ip_address = decimal_host_min_ip_address[:-1]
    # calculate host maximal ip address
    binary_host_max_ip_address = binary_broadcast_ip_address[:-1] + '0'
    split_binary_host_max_ip_address = re.findall('........', binary_host_max_ip_address)
    for x in range(4):
        decimal_host_max_ip_address += str(int(split_binary_host_max_ip_address[x], 2)) + '.'
    decimal_host_max_ip_address = decimal_host_max_ip_address[:-1]
    ################
    print(f"IP address   | (10) {ip_address}   | (2) {binary_ip_address}")
    print(f"Subnet mask  | (10) {decimal_subnet_mask} | (2) {binary_subnet_mask} | (bit) {subnet_mask}")
    print(f"Network size | {network_size}")
    print(f"Broadcast    | (10) {decimal_broadcast_ip_address} | (2) {binary_broadcast_ip_address}")
    print(f"Network      | (10) {decimal_network_ip_address}   | (2) {binary_network_ip_address}")
    print(f"Host minimal | (10) {decimal_host_min_ip_address}  | (2) {binary_host_min_ip_address}")
    print(f"Host maximal | (10) {decimal_host_max_ip_address}  | (2) {binary_host_max_ip_address}")
    ################
    # host input processing
    print("Input host number:")
    while True:
        host_number = input()
        if int(host_number) >= network_size:
            print("Entered host number is outside the network size. Input again.")
        else:
            break
    binary_host_number_ip_address = binary_ip_address[:int(subnet_mask)] + str(bin(int(host_number))[2:].zfill(32 - int(subnet_mask)))
    split_binary_host_number_ip_address = re.findall('........', binary_host_number_ip_address)
    for x in range(4):
        decimal_host_number_ip_address += str(int(split_binary_host_number_ip_address[x], 2)) + '.'
    decimal_host_number_ip_address = decimal_host_number_ip_address[:-1]
    return "IP address of your host number is:  " + decimal_host_number_ip_address


print(check_ip4())
