#!/usr/bin/python3

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    retrieved_url = requests.get(url)
    ret_url = retrieved_url.headers
    print(ret_url.get('X-Request-Id'))
