#!/usr/bin/python3

import urllib
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as argv_url:
        r_argv_url = argv_url.read()
    get_info = argv_url.info()
    print(get_info['X-Request-Id'])
