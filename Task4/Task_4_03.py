import re
import operator


def count_user_agent(N):
    log = open('C:\\Users\\Aleksandr\\Desktop\\EPAM\\Python\\access_log\\access_log')
    first_regex_user_agent_list = []
    second_regex_user_agent_list = []
    line = log.readlines()
    #  Get "..." from log
    for x in range(10000):
        first_regex_user_agent_list.append(re.findall(r'"(.*?)"', line[x]))
    #  Convert list of "..." to string
    str_user_agent_list = ''.join([str(elem) for elem in first_regex_user_agent_list])
    #  Get _.../d.d_ from list of "..."
    second_regex_user_agent_list.append(re.findall(r' [a-zA-z]+/[0-9\.]+ ', str_user_agent_list))
    second_regex_user_agent_list = second_regex_user_agent_list[0]
    #  Get .../d.d from list of _.../d.d_
    second_regex_user_agent_list = [element[1:-1] for element in second_regex_user_agent_list]
    #  Remove inappropriate items from .../d.d list
    regex = re.compile(r'(.*?)Version(.*?)')
    second_regex_user_agent_list = [i for i in second_regex_user_agent_list if not regex.match(i)]
    temp_dict = {}
    for x in range(len(second_regex_user_agent_list)):
        #  Reverse sort of user agents by their count
        temp_dict = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True))
        #  If length of dictionary is less than N, then fill out the dictionary
        if len(temp_dict) < N:
            temp_dict[second_regex_user_agent_list[x]] = second_regex_user_agent_list.count(second_regex_user_agent_list[x])
        #  If length of dictionary is equal N, then replace user agent with the least number of repetitions with a new one
        if len(temp_dict) == N and second_regex_user_agent_list.count(second_regex_user_agent_list[x]) > list(temp_dict.values())[N - 1]:
            del temp_dict[list(temp_dict.keys())[list(temp_dict.values()).index(list(temp_dict.values())[N - 1])]]
            temp_dict[second_regex_user_agent_list[x]] = second_regex_user_agent_list.count(second_regex_user_agent_list[x])
    #  Reverse sort of user agents by their count
    temp_dict = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True))
    # Print dictionary line by line
    for key, value in temp_dict.items():
        print("%-12s %-25s %-10s %s" % ('User Agent:', key, 'Count: ', value))


print(count_user_agent(7))
