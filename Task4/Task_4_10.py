import re
from datetime import datetime


def max_request_frequency(N):
    log = open('C:\\Users\\Aleksandr\\Desktop\\EPAM\\Python\\access_log\\access_log')
    #  Get list of periods
    period_count = []
    for x in range(1, N+1, 1):
        period_count.append(x)
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
    for x in range(len(second_regex_time_list) - 1):
        difference = (datetime.strptime(second_regex_time_list[x], '%H:%M:%S') - datetime.strptime(
            second_regex_time_list[x + 1], '%H:%M:%S')).total_seconds()
        seconds_difference_list.append(difference)
    #  Adding the last element to seconds_difference_list that is lost when calculating the difference
    seconds_difference_list.append(0.0)
    #  Get total duration of requests
    second_regex_time_list.reverse()
    seconds_difference_list.reverse()
    for number_of_period in range(len(period_count)):
        dT = period_count[number_of_period] * 60
        #  Variables for max requests
        max_first_request = 0
        max_last_request = 0
        max_count_request = 0
        #  Get periods
        sum = 0
        current_count = 0
        prev_count = 1
        for i in range(len(seconds_difference_list)):
            sum = (sum + seconds_difference_list[i])
            current_count = current_count + 1
            #  Get number of requests for a specified period of time
            if sum >= dT:
                #  Check max_count_request
                if current_count > max_count_request:
                    max_count_request = current_count
                    max_first_request = second_regex_time_list[prev_count - 1]
                    max_last_request = second_regex_time_list[prev_count - 1 + current_count - 1]
                    prev_count += current_count
                    sum = 0
                    current_count = 0
        print("For period =", period_count[number_of_period], "minutes. Number of requests for a specified period of time:", current_count)
        print("During period:", max_first_request, "-", max_last_request)


print(max_request_frequency(5))
