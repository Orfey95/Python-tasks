import re
import operator


def count_domain():
    log = open('C:\\Users\\Aleksandr\\Desktop\\EPAM\\Python\\access_log\\access_log')
    regex_domain_list = []
    line = log.readlines()
    #  Get domain from log
    for x in range(len(line)):
        regex_domain_list.append(str((re.findall(r'"(?:http|https)://(.+?)(?:/|").+?"', line[x])))[2:-2])
    temp_dict = {}
    for x in range(len(regex_domain_list)):
        if regex_domain_list[x] != '':
            temp_dict[regex_domain_list[x]] = regex_domain_list.count(regex_domain_list[x])
    #  Reverse sort of domains by their count
    temp_dict = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True))
    # Print dictionary line by line
    for key, value in temp_dict.items():
        print('Count: ', value, 'Domain: ', key)


print(count_domain())
