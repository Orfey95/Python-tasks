import re
import operator


def count_max_link_to_slash(N, K):
    log = open('C:\\Users\\Aleksandr\\Desktop\\EPAM\\Python\\access_log\\access_log')
    first_regex_link_list = []
    line = log.readlines()
    #  Get /link from log
    for x in range(1000):
        first_regex_link_list.append(str((re.findall(r'(?:GET|POST) (.+?) HTTP/1.1', line[x])))[2:-2])
    short_form_list = []
    for x in range(len(first_regex_link_list)):
        slash_list = re.split('/', first_regex_link_list[x])
        if K <= len(slash_list):
            str_tmp = ''
            for y in range(K):
                str_tmp += slash_list[y] + '/'
            short_form_list.append(str_tmp[:-1])
        else:
            str_tmp = ''
            for y in range(len(slash_list)):
                str_tmp += slash_list[y] + '/'
            short_form_list.append(str_tmp[:-1])
    temp_dict = {}
    for x in range(len(short_form_list)):
        #  Reverse sort of links by their count
        temp_dict = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True))
        #  If length of dictionary is less than N, then fill out the dictionary
        if len(temp_dict) < N:
            temp_dict[short_form_list[x]] = short_form_list.count(short_form_list[x])
        #  If length of dictionary is equal N, then replace link with the least number of repetitions with a new one
        if len(temp_dict) == N and short_form_list.count(short_form_list[x]) > list(temp_dict.values())[N - 1]:
            del temp_dict[list(temp_dict.keys())[list(temp_dict.values()).index(list(temp_dict.values())[N - 1])]]
            temp_dict[short_form_list[x]] = short_form_list.count(short_form_list[x])
    #  Reverse sort of links by their count
    temp_dict = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True))
    # Print dictionary line by line
    for key, value in temp_dict.items():
        print('Count: ', value, 'URL: ', key)


print(count_max_link_to_slash(4, 4))
