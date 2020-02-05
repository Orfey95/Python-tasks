import re
import operator


def count_max_and_min_link(N):
    log = open('access_log')
    regex_link_list = []
    line = log.readlines()
    #  Get /link from log
    for x in range(len(line)):
        regex_link_list.append(str((re.findall(r"(?:GET|POST) (.+?) HTTP/1.1", line[x])))[2:-2])
    max_len_dict = {}
    min_len_dict = {}
    for x in range(len(regex_link_list)):
        #  Reverse sort of links by their count
        max_len_dict = dict(sorted(max_len_dict.items(), key=operator.itemgetter(1), reverse=True))
        min_len_dict = dict(sorted(min_len_dict.items(), key=operator.itemgetter(1), reverse=True))
        #  If length of dictionary is less than N, then fill out the dictionary
        if len(max_len_dict) < N:
            max_len_dict[regex_link_list[x]] = len(regex_link_list[x])
        #  If length of dictionary is equal N, then replace link with the smallest length with a new one
        if len(max_len_dict) == N and len(regex_link_list[x]) > list(max_len_dict.values())[N - 1]:
            del max_len_dict[list(max_len_dict.keys())[list(max_len_dict.values()).index(list(max_len_dict.values())[N - 1])]]
            max_len_dict[regex_link_list[x]] = len(regex_link_list[x])
        #  If length of dictionary is less than N, then fill out the dictionary
        if len(min_len_dict) < N and len(regex_link_list[x]) >= 1:
            min_len_dict[regex_link_list[x]] = len(regex_link_list[x])
        #  If length of dictionary is equal N, then replace link with the longest length with a new one
        if len(min_len_dict) == N and len(regex_link_list[x]) < list(min_len_dict.values())[0] and len(regex_link_list[x]) >= 1:
            del min_len_dict[list(min_len_dict.keys())[list(min_len_dict.values()).index(list(min_len_dict.values())[0])]]
            min_len_dict[regex_link_list[x]] = len(regex_link_list[x])
    #  Reverse sort of links by their count
    max_len_dict = dict(sorted(max_len_dict.items(), key=operator.itemgetter(1), reverse=True))
    min_len_dict = dict(sorted(min_len_dict.items(), key=operator.itemgetter(1)))
    # Print dictionary line by line
    print("The list of links with the maximum length:")
    for key, value in max_len_dict.items():
        print("%-12s %-25s %-10s %s" % ('Length:', value, 'URL:', key))
    print("The list of links with the minimum length:")
    for key, value in min_len_dict.items():
        print("%-12s %-25s %-10s %s" % ('Length:', value, 'URL:', key))


print(count_max_and_min_link(7))
