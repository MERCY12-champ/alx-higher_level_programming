#!/usr/bin/python3
"""A function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """Script to transforme a string into json object"""

    return json.loads(my_str)
