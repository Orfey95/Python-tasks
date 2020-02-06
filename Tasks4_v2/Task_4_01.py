import re
from collections import Counter


def count_ip(N):
    log = open('access_log')
    regex_ip_list = []
    line = log.readlines()
    #  Get ip address from log
    for x in range(len(line)):
        regex_ip_list.append(str((re.findall(r'\((\d+\.\d+\.\d+\.\d+)', line[x])))[2:-2])
    #  Counter for ip addresses
    temp_dict = Counter(regex_ip_list)
    # Print dictionary line by line
    for key, value in temp_dict.most_common(N):
        print('Count: ', value, 'IP address: ', key)


print(count_ip(7))
