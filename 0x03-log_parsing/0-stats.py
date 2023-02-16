#!/usr/bin/python3
"""log parser"""
import sys



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
