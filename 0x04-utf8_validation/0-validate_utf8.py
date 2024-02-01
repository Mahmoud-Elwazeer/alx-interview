#!/usr/bin/python3
"""import libraries"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""
    for i in data:
        if i >= 256 or i < -128:
            return False

    return True
