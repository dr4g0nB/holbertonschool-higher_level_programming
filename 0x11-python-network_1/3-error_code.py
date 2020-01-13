#!/usr/bin/python3

import sys
import urllib
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as url_data:
            r_url = url_data.read()
            print(r_url.decode("UTF-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
