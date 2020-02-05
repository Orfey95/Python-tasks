import re
from collections import Counter


def count_ip(N):
    log = open('access_log')
    first_regex_ip_list = []
    second_regex_ip_list = []
    line = log.readlines()
    #  Get (...) from log
    for x in range(len(line)):
        first_regex_ip_list.append(re.findall(r'\([^"]+\)', line[x]))
    #  Convert list of (...) to string
    str_ip_list = ''.join([str(elem) for elem in first_regex_ip_list])
    #  Get d.d.d.d from list of (...)
    second_regex_ip_list.append(re.findall(r'\d+\.\d+\.\d+\.\d+', str_ip_list))
    second_regex_ip_list = second_regex_ip_list[0]
    #  Counter for ip addresses
    temp_dict = Counter(second_regex_ip_list)
    # Print dictionary line by line
    for key, value in temp_dict.most_common(N):
        print('Count: ', value, 'IP address: ', key)


print(count_ip(7))
