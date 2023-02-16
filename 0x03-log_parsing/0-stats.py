#!/usr/bin/python3
"""log parser"""
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

# check status code
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    code = int(line_arr[-2])
    if (code not in status_codes):
        return False
    return True


codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0
total_size = 0
try:
    for line in sys.stdin:
        if (checkline(line)):
            line_arr = line.split()
            code = int(line_arr[-2])
            file_size = int(line_arr[-1])
            total_size += file_size
            codes[code] = codes.get(code) + 1
        line_count += 1

        if line_count == 10:
            line_count = 0
            print(f'File size: {total_size}')
            for key, value in sorted(codes.items()):
                if (value != 0):
                    print(f'{key}: {value}')
except Exception as err:
    pass

finally:
    print(f'File size: {total_size}')
    for key, value in sorted(codes.items()):
        if (value != 0):
            print(f'{key}: {value}')

