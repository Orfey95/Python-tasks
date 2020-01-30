import re
import operator


def count_ip(N):
    log = open('C:\\Users\\Aleksandr\\Desktop\\EPAM\\Python\\access_log\\access_log')
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
    temp_dict = {}
    for x in range(len(second_regex_ip_list)):
        #  Reverse sort of ip addresses by their count
        temp_dict = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True))
        #  If length of dictionary is less than N, then fill out the dictionary
        if len(temp_dict) < N:
            temp_dict[second_regex_ip_list[x]] = second_regex_ip_list.count(second_regex_ip_list[x])
        #  If length of dictionary is equal N, then replace ip with the least number of repetitions with a new one
        if len(temp_dict) == N and second_regex_ip_list.count(second_regex_ip_list[x]) > list(temp_dict.values())[N-1]:
            del temp_dict[list(temp_dict.keys())[list(temp_dict.values()).index(list(temp_dict.values())[N-1])]]
            temp_dict[second_regex_ip_list[x]] = second_regex_ip_list.count(second_regex_ip_list[x])
    #  Reverse sort of ip addresses by their count
    temp_dict = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True))
    # Print dictionary line by line
    for key, value in temp_dict.items():
        print('Count: ', value, 'IP address: ', key)


print(count_ip(7))
