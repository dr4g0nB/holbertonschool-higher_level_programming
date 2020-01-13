#!/usr/bin/python3

import urllib
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as retrieved_data:
        data = retrieved_data.read()
        html = data.decode()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
        print("\t- utf8 content:", html)

