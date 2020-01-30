import re
import operator
from datetime import datetime


def error_code_frequency(dT):
    log = open('C:\\Users\\Aleksandr\\Desktop\\EPAM\\Python\\access_log\\access_log')
    # Lists for work with error codes
    first_regex_error_code_list = []
    second_regex_error_code_list = []
    # Lists for work with time
    first_regex_time_list = []
    second_regex_time_list = []
    seconds_difference_list = []
    line = log.readlines()
    for x in range(len(line)):
        #  Get _ddd from log
        first_regex_error_code_list.append(re.findall(r'" \d{3}', line[x]))
        #  Get [...] from log
        first_regex_time_list.append(re.findall(r'\[[^"]+\]', line[x]))
    #  Convert list of ddd to string
    str_error_code_list = ''.join([str(elem) for elem in first_regex_error_code_list])
    #  Get ddd from list of _ddd
    second_regex_error_code_list.append(re.findall(r'\d{3}', str_error_code_list))
    second_regex_error_code_list = second_regex_error_code_list[0]
    #  Convert list of [...] to string
    str_time_list = ''.join([str(elem) for elem in first_regex_time_list])
    #  Get :d:d:d from list of [...]
    second_regex_time_list.append(re.findall(r'\:\d{2}\:\d{2}\:\d{2}', str_time_list))
    second_regex_time_list = second_regex_time_list[0]
    #  Get d:d:d from list of :d:d:d
    second_regex_time_list = [element[1:] for element in second_regex_time_list]
    second_regex_time_list.sort()
    second_regex_time_list.reverse()
    #  Get seconds difference
    for x in range(len(second_regex_time_list) - 1):
        difference = (datetime.strptime(second_regex_time_list[x], '%H:%M:%S') - datetime.strptime(
            second_regex_time_list[x + 1], '%H:%M:%S')).total_seconds()
        seconds_difference_list.append(difference)
    #  Adding the last element to seconds_difference_list that is lost when calculating the difference
    seconds_difference_list.append(0.0)
    #  Get total duration of requests
    second_regex_time_list.reverse()
    seconds_difference_list.reverse()
    total_sum = 0
    for i in seconds_difference_list:
        total_sum = total_sum + i
    print("Total duration of requests:", total_sum, "seconds")
    print("Total duration of requests:", total_sum / 60, "minutes")
    print("Time of first request:", second_regex_time_list[0])
    print("Time of last request:", second_regex_time_list[len(second_regex_time_list) - 1])
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
            print("Period:", second_regex_time_list[prev_count - 1], "-",
                  second_regex_time_list[prev_count - 1 + current_count - 1])
            print("Number of requests for a specified period of time:", current_count)
            #  Calculate error code statistic
            for x in range((prev_count - 1), (prev_count - 1 + current_count - 1)):
                temp_error_code_list.append(second_regex_error_code_list[x])
            count_error_code_dict = {}
            for x in range(len(temp_error_code_list)):
                count_error_code_dict[temp_error_code_list[x]] = temp_error_code_list.count(temp_error_code_list[x])
            #  Reverse sort of error statistic dictionary
            count_error_code_dict = dict(sorted(count_error_code_dict.items(), key=operator.itemgetter(1), reverse=True))
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
            print("Period:", second_regex_time_list[prev_count - 1], "-",
                  second_regex_time_list[prev_count - 1 + current_count - 1])
            print("Number of requests for a remainder period of time:", current_count)
            #  Calculate error code statistic
            for x in range((prev_count - 1), (prev_count - 1 + current_count - 1)):
                temp_error_code_list.append(second_regex_error_code_list[x])
            count_error_code_dict = {}
            for x in range(len(temp_error_code_list)):
                count_error_code_dict[temp_error_code_list[x]] = temp_error_code_list.count(temp_error_code_list[x])
            #  Reverse sort of error statistic dictionary
            count_error_code_dict = dict(
                sorted(count_error_code_dict.items(), key=operator.itemgetter(1), reverse=True))
            for key, value in count_error_code_dict.items():
                print('Error code: ', key, ' Count: ', value)
            ###########


print(error_code_frequency(5))
