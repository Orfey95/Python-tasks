import re
import operator
from datetime import datetime


def count_ip(N):
    log = open('C:\\Users\\Aleksandr\\Desktop\\EPAM\\Python\\access_log\\access_log')
    first_regex_ip_list = []
    second_regex_ip_list = []
    line = log.readlines()
    #  Get (...) from log
    for x in range(len(line)):
        first_regex_ip_list.append(re.findall(r'\([^"]+\)', line[x]))
    #  Convert list of (...) to string
    str_ip_list = ''.join([str(elem) for elem in first_regex_ip_list])
    #  Get d.d.d.d from list of (...)
    second_regex_ip_list.append(re.findall(r'\d+\.\d+\.\d+\.\d+', str_ip_list))
    second_regex_ip_list = second_regex_ip_list[0]
    temp_dict = {}
    for x in range(len(second_regex_ip_list)):
        #  Reverse sort of ip addresses by their count
        temp_dict = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True))
        #  If length of dictionary is less than N, then fill out the dictionary
        if len(temp_dict) < N:
            temp_dict[second_regex_ip_list[x]] = second_regex_ip_list.count(second_regex_ip_list[x])
        #  If length of dictionary is equal N, then replace ip with the least number of repetitions with a new one
        if len(temp_dict) == N and second_regex_ip_list.count(second_regex_ip_list[x]) > list(temp_dict.values())[N-1]:
            del temp_dict[list(temp_dict.keys())[list(temp_dict.values()).index(list(temp_dict.values())[N-1])]]
            temp_dict[second_regex_ip_list[x]] = second_regex_ip_list.count(second_regex_ip_list[x])
    #  Reverse sort of ip addresses by their count
    temp_dict = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True))
    # Print dictionary line by line
    for key, value in temp_dict.items():
        print('Count: ', value, 'IP address: ', key)


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
    total_sum = 0
    for i in seconds_difference_list:
        total_sum = total_sum + i
    print("Total duration of requests:", total_sum, "seconds")
    print("Total duration of requests:", total_sum/60, "minutes")
    print("Time of first request:", second_regex_time_list[len(second_regex_time_list) - 1])
    print("Time of last request:", second_regex_time_list[0])
    print("The period you specify is:", dT, "minutes")
    dT = dT*60
    print("The period you specify is:", dT, "seconds")
    #  Get periods
    sum = 0
    current_count = 0
    prev_count = 0
    for i in range(len(seconds_difference_list)):
        sum = (sum + seconds_difference_list[i])
        current_count = current_count + 1
        #  Get number of requests for a specified period of time
        if sum >= dT:
            print("Period:", second_regex_time_list[prev_count + current_count - 1], "-", second_regex_time_list[prev_count - 1])
            print("Number of requests for a specified period of time:", current_count)
            prev_count = current_count
            sum = 0
            current_count = 0
        #  Get number of requests for a remainder period of time
        if sum < dT and i == len(seconds_difference_list) - 1:
            print("The remainder:", sum, "seconds")
            print("Number of requests for a remainder period of time:", current_count)
            print("Period:", second_regex_time_list[prev_count + current_count - 1], "-", second_regex_time_list[prev_count - 1])


print(request_frequency(7))
