import re
from collections import Counter

def count_user_agent(N):
    log = open('access_log')
    regex_user_agent_list = []
    line = log.readlines()
    #  Get "..." from log
    for x in range(len(line)):
        if str(re.findall(r'" "(.*?)" "ajp', line[x]))[2:-2] != '-':
            regex_user_agent_list.append(str(re.findall(r'" "(.*?)" "ajp', line[x]))[2:-2])
    #  Counter for user agents
    user_agents_dict = Counter(regex_user_agent_list)
    # Print dictionary line by line
    for key, value in user_agents_dict.most_common(N):
            print("%-8s %-10s %-10s %s" % ('Count: ', value, 'User Agent:', key))


print(count_user_agent(7))
