import re
from datetime import datetime
from collections import Counter


def upstream_frequency(dT):
    log = open('access_log')
    #  Get list of periods
    period_count = [dT]
    # Lists for work with time
    regex_time_list = []
    seconds_difference_list = []
    regex_domain_list = []
    line = log.readlines()
    for x in range(len(line)):
        #  Get time from log
        regex_time_list.append(str((re.findall(r'\[.+?\:(\d{2}\:\d{2}\:\d{2}).+?\]', line[x])))[2:-2])
        #  Get upstream from log
        regex_domain_list.append(str((re.findall(r'"(\w+://\d+\.\d+\.\d+\.\d+:\d+)"', line[x])))[2:-2])
    regex_time_list, regex_domain_list = (list(t) for t in zip(*sorted(zip(regex_time_list, regex_domain_list))))
    regex_domain_list.reverse()
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
    total_sum = 0
    for i in seconds_difference_list:
        total_sum = total_sum + i
    print("Total duration of requests:", total_sum, "seconds")
    print("Total duration of requests:", total_sum / 60, "minutes")
    print("Time of first request:", regex_time_list[0])
    print("Time of last request:", regex_time_list[len(regex_time_list) - 1])
    for number_of_period in range(len(period_count)):
        dT = period_count[number_of_period] * 60
        print("The period you specify is:", dT/60, "minutes")
        print("The period you specify is:", dT, "seconds")
        #  Get periods
        sum = 0
        current_count = 0
        prev_count = 1
        temp_upstream_list = []
        for i in range(len(seconds_difference_list)):
            sum = (sum + seconds_difference_list[i])
            current_count = current_count + 1
            #  Get number of requests for a specified period of time
            if sum >= dT:
                print("Period:", regex_time_list[prev_count - 1], "-",
                      regex_time_list[prev_count - 1 + current_count - 1])
                print("Number of requests for a specified period of time:", current_count)
                #  Calculate upstream statistic
                for x in range((prev_count - 1), (prev_count - 1 + current_count - 1)):
                    temp_upstream_list.append(regex_domain_list[x])
                count_upstream_dict = Counter(temp_upstream_list)
                for key, value in count_upstream_dict.items():
                    if key != '':
                        print('Count: ', value, 'Upstream: ', key)
                ###########
                prev_count += current_count
                sum = 0
                current_count = 0
                temp_upstream_list.clear()
            #  Get number of requests for a remainder period of time
            if sum < dT and i == len(seconds_difference_list) - 1:
                print("The remainder:", sum, "seconds")
                print("Period:", regex_time_list[prev_count - 1], "-",
                      regex_time_list[prev_count - 1 + current_count - 1])
                print("Number of requests for a remainder period of time:", current_count)
                #  Calculate upstream statistic
                for x in range((prev_count - 1), (prev_count - 1 + current_count - 1)):
                    temp_upstream_list.append(regex_domain_list[x])
                count_upstream_dict = Counter(temp_upstream_list)
                for key, value in count_upstream_dict.items():
                    if key != '':
                        print('Count: ', value, 'Upstream: ', key)
