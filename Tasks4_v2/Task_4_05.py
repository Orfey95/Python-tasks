import re
from collections import Counter


def count_max_and_min_link(N):
    log = open('C:\\Users\\Aleksandr\\Desktop\\EPAM\\Python\\access_log\\access_log')
    regex_link_list = []
    line = log.readlines()
    #  Get /link from log
    for x in range(len(line)):
        if len(str(re.findall(r"(?:GET|POST) (.+?) HTTP/1.1", line[x]))[2:-2]) >= 2:
            regex_link_list.append(str(re.findall(r"(?:GET|POST) (.+?) HTTP/1.1", line[x]))[2:-2])
    #  Counter for links
    count_link_dict = Counter(regex_link_list)
    new_d = {}
    new_d2 = {}
    for k in sorted(count_link_dict, key=len):
        new_d[k] = count_link_dict[k]
    # Get first N items in dictionary
    print("The list of links with the minimum length:")
    out = dict(list(new_d.items())[0: N])
    if N <= len(new_d):
        # Print dictionary
        for key, value in out.items():
            print("%-10s %-10s %-10s %-5s %-10s %s" % ('Length: ', len(key), 'Count: ', value, 'URL: ', key))
    else:
        N = len(new_d)
        # Print dictionary
        for key, value in out.items():
            print("%-10s %-10s %-10s %-5s %-10s %s" % ('Length: ', len(key), 'Count: ', value, 'URL: ', key))
    for k in sorted(count_link_dict, key=len, reverse=True):
        new_d2[k] = count_link_dict[k]
    # Get first N items in dictionary
    print("The list of links with the maximum length:")
    out2 = dict(list(new_d2.items())[0: N])
    if N <= len(new_d2):
        # Print dictionary
        for key, value in out2.items():
            print("%-10s %-10s %-10s %-5s %-10s %s" % ('Length: ', len(key), 'Count: ', value, 'URL: ', key))
    else:
        N = len(new_d2)
        # Print dictionary
        for key, value in out2.items():
            print("%-10s %-10s %-10s %-5s %-10s %s" % ('Length: ', len(key), 'Count: ', value, 'URL: ', key))


print(count_max_and_min_link(7))
