#!/usr/bin/python3

import urllib
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as retrieved_data:
    data = retrieved_data.read()
    html = data.decode("UTF-8")
    print("Body response:")
    print("\t - type: {}".format(type(data)))
    print("\t - content: {}".format(data))
    print("\t - utf8 content: {}".format(html))

