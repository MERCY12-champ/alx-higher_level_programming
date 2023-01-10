#!/usr/bin/python3
"""A function that writes an Object to
a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Script to write an object to text using
json representation"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
