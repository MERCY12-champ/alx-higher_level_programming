#!/usr/bin/python3
"""import json modules"""
import json


def load_from_json_file(filename):
    """Script to create an object from json file"""

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
