import re
from collections import Counter


def count_max_link_to_slash(N, K):
    log = open('access_log')
    first_regex_link_list = []
    line = log.readlines()
    #  Get /link from log
    for x in range(len(line)):
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
    #  Counter for ip addresses
    temp_dict = Counter(short_form_list)
    # Print dictionary line by line
    for key, value in temp_dict.most_common(N):
        print('Count: ', value, 'URL: ', key)


print(count_max_link_to_slash(7, 4))
