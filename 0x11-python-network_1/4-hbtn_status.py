#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status.
"""

import requests


def main():
    """
    Sends a GET request to https://intranet.hbtn.io/status and
    displays the body of the response.
    """
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)

    if response.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
