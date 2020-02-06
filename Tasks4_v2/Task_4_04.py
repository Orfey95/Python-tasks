import re
from collections import Counter
from datetime import datetime


def error_code_frequency(dT):
    log = open('access_log')
    # Lists for work with error codes
    first_regex_error_code_list = []
    second_regex_error_code_list = []
    # List for work with time
    regex_time_list = []
    seconds_difference_list = []
    line = log.readlines()
    for x in range(len(line)):
        #  Get error code from log
        first_regex_error_code_list.append(str((re.findall(r'" \d{3}', line[x])))[4:-2])
        #  Get time from log
        regex_time_list.append(str((re.findall(r'\[.+?\:(\d{2}\:\d{2}\:\d{2}).+?\]', line[x])))[2:-2])
    regex_time_list, first_regex_error_code_list = (list(t) for t in zip(*sorted(zip(regex_time_list, first_regex_error_code_list))))
    first_regex_error_code_list.reverse()
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
    print("The period you specify is:", dT, "minutes")
    dT = dT * 60
    print("The period you specify is:", dT, "seconds")
    #  Get periods
    sum = 0
    current_count = 0
    prev_count = 1
    temp_error_code_list = []
    for i in range(len(seconds_difference_list)):
        sum = (sum + seconds_difference_list[i])
        current_count = current_count + 1
        #  Get number of requests for a specified period of time
        if sum >= dT:
            print("Period:", regex_time_list[prev_count - 1], "-",
                  regex_time_list[prev_count - 1 + current_count - 1])
            print("Number of requests for a specified period of time:", current_count)
            #  Calculate error code statistic
            for x in range((prev_count - 1), (prev_count - 1 + current_count - 1)):
                if re.match(r'50\d', first_regex_error_code_list[x]):
                    temp_error_code_list.append(first_regex_error_code_list[x])
            #  Counter for error statuses
            count_error_code_dict = Counter(temp_error_code_list)
            for key, value in count_error_code_dict.items():
                print('Error code: ', key, ' Count: ', value)
            ###########
            prev_count += current_count
            sum = 0
            current_count = 0
            temp_error_code_list.clear()
        #  Get number of requests for a remainder period of time
        if sum < dT and i == len(seconds_difference_list) - 1:
            print("The remainder:", sum, "seconds")
            print("Period:", regex_time_list[prev_count - 1], "-",
                  regex_time_list[prev_count - 1 + current_count - 1])
            print("Number of requests for a remainder period of time:", current_count)
            #  Calculate error code statistic
            for x in range((prev_count - 1), (prev_count - 1 + current_count - 1)):
                if re.match(r'50\d', first_regex_error_code_list[x]):
                    temp_error_code_list.append(first_regex_error_code_list[x])
            #  Counter for error statuses
            count_error_code_dict = Counter(temp_error_code_list)
            for key, value in count_error_code_dict.items():
                print('Error code: ', key, ' Count: ', value)

print(error_code_frequency(3))
