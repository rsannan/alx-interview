#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys
import re


def checkline(line):
    """Check for valid line"""
    line_arr = line.split()

# check ip address
    ip_address = re.compile(r'\d+.\d+.\d+.\d+')
    ip = ip_address.search(line)
    if (ip.group() != line_arr[0]):
        return False

# check date
    date_pattern = re.compile(r'[\d]{4}-[\d]{2}-[\d]{2}')
    date = date_pattern.search(line)
    if (date.group() != line_arr[2][1:]):
        return False

# check time
    time_pattern = re.compile(r'[\d]{2}:[\d]{2}:[\d]{2}.\d+')
    time = time_pattern.search(line)
    if (time.group() != line_arr[3][:-1]):
        return False

# check http string
    http_string = line_arr[4] + line_arr[5] + line_arr[6]
    http_pattern = '"GET/projects/260HTTP/1.1"'
    if (http_string != http_pattern):
        return False

    return True


cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if checkline(line):
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
