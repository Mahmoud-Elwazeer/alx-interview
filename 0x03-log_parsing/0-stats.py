#!/usr/bin/python3
"""import libraries"""
import sys


def print_stats(size: int, dict: dict) -> None:
    """print specific format"""
    print('File size: {}'.format(size))
    for key, value in dict.items():
        if value:
            print('{}: {}'.format(key, value))


def main() -> None:
    """main function"""

    """initial values"""
    count = 0
    size = 0
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
    try:
        for line in sys.stdin:
            count += 1
            if count == 11:
                print_stats(size, out)
                count = 0
                size = 0
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

            """convert data to list to manage"""
            data = line.split()

            """calc size"""
            try:
                size += int(data[-1])
            except Exception:
                pass
            try:
                str_status = data[-2]
                out[str_status] += 1
            except Exception:
                pass
        print_stats(size, out)
    except KeyboardInterrupt:
        print_stats(size, out)
        raise


if __name__ == '__main__':
    main()
