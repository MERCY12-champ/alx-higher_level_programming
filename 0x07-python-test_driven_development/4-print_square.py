#!/usr/bin/python3
"""prints a square with the character #"""


def print_square(size):
    """prints a square with the character #"""
    size = int(size)

    for i in range(size):
        for r in range(size):
            print('#', end="")
        print("")
    if size is int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')