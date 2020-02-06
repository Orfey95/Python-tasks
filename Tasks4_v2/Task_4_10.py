import re
from datetime import datetime


def max_request_frequency(N, dT):
    log = open('access_log')
    regex_time_list = []
    seconds_difference_list = []
    line = log.readlines()
    #  Get time from log
    for x in range(len(line)):
        regex_time_list.append(str((re.findall(r'\[.+?\:(\d{2}\:\d{2}\:\d{2}).+?\]', line[x])))[2:-2])
    regex_time_list.sort()
    regex_time_list.reverse()
    #  Get seconds difference
    for x in range(len(regex_time_list) - 1):
        difference = (datetime.strptime(regex_time_list[x], '%H:%M:%S') - datetime.strptime(
            regex_time_list[x + 1], '%H:%M:%S')).total_seconds()
        seconds_difference_list.append(difference)
    #  Adding the last element to seconds_difference_list that is lost when calculating the difference
    seconds_difference_list.append(0.0)
    #  Get total duration of requests
    regex_time_list.reverse()
    seconds_difference_list.reverse()
    dT = dT * 60
    #  Get periods
    sum = 0
    current_count = 0
    prev_count = 1
    default_data = {}
    for i in range(len(seconds_difference_list)):
        sum = (sum + seconds_difference_list[i])
        current_count = current_count + 1
        #  Get number of requests for a specified period of time
        if sum >= dT:
            t_str = str(regex_time_list[prev_count - 1]) + ' - ' + str(
                regex_time_list[prev_count - 1 + current_count - 1])
            default_data.update({t_str: int(current_count)})
            prev_count += current_count
            sum = 0
            current_count = 0
    default_data = dict(sorted(default_data.items(), key=lambda x: x[1], reverse=True))
    # Get first K items in dictionary
    out = dict(list(default_data.items())[0: N])
    if N <= len(default_data):
        # Print dictionary line by line
        for key, value in out.items():
            print("%-15s %-25s %-10s %s" % ('During period:', key, 'Count:', value))
    else:
        N = len(default_data)
        # Print dictionary line by line
        for key, value in out.items():
            print("%-15s %-20s %-10s %s" % ('During period:', key, 'Count:', value))

