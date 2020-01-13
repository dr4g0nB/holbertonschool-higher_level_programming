#!/usr/bin/python3

import urllib
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as retrieved_data:
        data = retrieved_data.read()
        html = data.decode()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
        print("\t- utf8 content:", html)
