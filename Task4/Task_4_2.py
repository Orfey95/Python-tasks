import re
from datetime import datetime


def request_frequency(dT):
    log = open('C:\\Users\\Aleksandr\\Desktop\\EPAM\\Python\\access_log\\access_log')
    first_regex_time_list = []
    second_regex_time_list = []
    seconds_difference_list = []
    line = log.readlines()
    #  Get [...] from log
    for x in range(len(line)):
        first_regex_time_list.append(re.findall(r'\[[^"]+\]', line[x]))
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
    for x in range(len(second_regex_time_list)-1):
        difference = (datetime.strptime(second_regex_time_list[x], '%H:%M:%S') - datetime.strptime(second_regex_time_list[x+1], '%H:%M:%S')).total_seconds()
        seconds_difference_list.append(difference)
    #  Adding the last element to seconds_difference_list that is lost when calculating the difference
    seconds_difference_list.append(0.0)
    #  Get total duration of requests
    second_regex_time_list.reverse()
    print(second_regex_time_list)
    seconds_difference_list.reverse()
    print(seconds_difference_list)
    total_sum = 0
    for i in seconds_difference_list:
        total_sum = total_sum + i
    print("Total duration of requests:", total_sum, "seconds")
    print("Total duration of requests:", total_sum/60, "minutes")
    print("Time of first request:", second_regex_time_list[0])
    print("Time of last request:", second_regex_time_list[len(second_regex_time_list) - 1])
    print("The period you specify is:", dT, "minutes")
    dT = dT*60
    print("The period you specify is:", dT, "seconds")
    #  Get periods
    sum = 0
    current_count = 0
    prev_count = 1
    for i in range(len(seconds_difference_list)):
        sum = (sum + seconds_difference_list[i])
        current_count = current_count + 1
        #  Get number of requests for a specified period of time
        if sum >= dT:
            print("Period:", second_regex_time_list[prev_count - 1], "-", second_regex_time_list[prev_count - 1 + current_count - 1])
            print("Number of requests for a specified period of time:", current_count)
            prev_count += current_count
            sum = 0
            current_count = 0
        #  Get number of requests for a remainder period of time
        if sum < dT and i == len(seconds_difference_list) - 1:
            print("The remainder:", sum, "seconds")
            print("Period:", second_regex_time_list[prev_count - 1], "-", second_regex_time_list[prev_count - 1 + current_count - 1])
            print("Number of requests for a remainder period of time:", current_count)


print(request_frequency(4))
