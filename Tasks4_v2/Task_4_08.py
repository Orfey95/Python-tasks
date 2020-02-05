import re
from collections import Counter


def count_domain():
    log = open('access_log')
    regex_domain_list = []
    line = log.readlines()
    #  Get domain from log
    for x in range(len(line)):
        regex_domain_list.append(str((re.findall(r'"(?:http|https)://(.+?)(?:/|").+?"', line[x])))[2:-2])
    temp_dict = Counter(regex_domain_list)
    # Print dictionary line by line
    for key, value in temp_dict.most_common():
        if key != '':
            print('Count: ', value, 'Domain: ', key)


print(count_domain())
