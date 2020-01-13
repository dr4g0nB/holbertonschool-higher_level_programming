#!/usr/bin/python3

import urllib
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': sys.argv[2]}

    email_data = urllib.parse.urlencode(values)
    email_data = email_data.encode('ascii')
    req = urllib.request.Request(url, email_data)

    with urllib.request.urlopen(req) as re_data:
        r_re_data = re_data.read()
        print(r_re_data.decode("UTF-8"))
