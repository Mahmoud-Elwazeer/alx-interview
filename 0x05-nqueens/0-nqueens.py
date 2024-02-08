#!/usr/bin/python3
""" import libraries"""
import sys


def main(n):
    """The N queens puzzle"""
    pass


if __name__ == "__main__":
    if ((len(sys.argv) != 2)):
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        if (not isinstance(int(sys.argv[1]), int)):
            print("N must be a number")
            sys.exit(1)
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if (int(sys.argv[1]) < 4):
        print("N must be at least 4")
        sys.exit(1)
    main(int(sys.argv[1]))
