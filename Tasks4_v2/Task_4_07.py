import re
from collections import Counter


def count_upstream():
    log = open('access_log')
    regex_upstream_list = []
    line = log.readlines()
    #  Get upstream from log
    for x in range(len(line)):
        regex_upstream_list.append(str((re.findall(r'"(\w+://\d+\.\d+\.\d+\.\d+:\d+)"', line[x])))[2:-2])
    temp_dict = Counter(regex_upstream_list)
    # Print dictionary line by line
    for key, value in temp_dict.most_common():
        if key != '':
            print('Count: ', value, 'Upstream: ', key)


print(count_upstream())
