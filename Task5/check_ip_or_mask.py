def check_ip_or_mask(temp_str):
    IPv4_regex = (r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}')
    temp_list_ip_mask = re.findall(IPv4_regex, temp_str)
    binary_temp_list_ip_mask = []
    temp_binary_ip_mask = ''
    for x in range(len(temp_list_ip_mask)):
        split_ip_address = re.split(r'\.', temp_list_ip_mask[x])
        for y in range(len(split_ip_address)):
            temp_binary_ip_mask += str(bin(int(split_ip_address[y]))[2:].zfill(8))
        binary_temp_list_ip_mask.append(temp_binary_ip_mask)
        temp_binary_ip_mask = ''
    ip_index_list = []
    mask_index_list = []
    for x in range(2):
        if not re.match(r'^[1]+[0]*$', binary_temp_list_ip_mask[x]):
            ip_index_list.append(x)
        if re.match(r'^[1]+[0]*$', binary_temp_list_ip_mask[x]):
            mask_index_list.append(x)
    if len(ip_index_list) == 1 and len(mask_index_list) == 1:
        ipv4 = temp_list_ip_mask[int(ip_index_list[0])]
        net_mask = temp_list_ip_mask[int(mask_index_list[0])]
    else:
        if (binary_temp_list_ip_mask[0].count('1')) < (binary_temp_list_ip_mask[0].count('1')):
            ipv4 = temp_list_ip_mask[0]
            net_mask = temp_list_ip_mask[1]
        else:
            ipv4 = temp_list_ip_mask[1]
            net_mask = temp_list_ip_mask[0]

    return "IPv4: " + ipv4 + "\n" + "Net mask: " + net_mask
