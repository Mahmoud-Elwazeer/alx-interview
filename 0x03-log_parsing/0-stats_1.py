#!/usr/bin/python3
"""import libraries"""
import sys


def main():
    """main function"""

    """initial values"""
    count = 0
    size = 0
    lst = []
    out = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

    for line in sys.stdin:
        try:
            count += 1
            if count == 11:
                print('File size: {}'.format(size))
                for key, value in out.items():
                    if value != 0:
                        print('{}: {}'.format(key, value))
                count = 0
                size = 0
                lst = []
                out = {
                    '200': 0,
                    '301': 0,
                    '400': 0,
                    '401': 0,
                    '403': 0,
                    '404': 0,
                    '405': 0,
                    '500': 0
                    }

            """get data from stdout and read each line"""
            lst.append(line)
            """convert data to list to manage"""
            data = line.split()

            """calc size"""
            size += int(data[-1])
            str_status = data[-2]
            out[str_status] += 1
        except Exception:
            pass


if __name__ == '__main__':
    main()
