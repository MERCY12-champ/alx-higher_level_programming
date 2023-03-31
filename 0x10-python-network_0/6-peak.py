#!/usr/bin/python3

"""
This module contains a function to find a peak in an unsorted list of integers.
"""

def find_peak(list_of_integers):
    """

    Finds a peak in an unsorted list of integers.

    Args:
        list_of_integers (list): List of integers to find a peak in.

    Returns:
        int: The peak value in the list.

    Complexity:
        O(log(n))
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
