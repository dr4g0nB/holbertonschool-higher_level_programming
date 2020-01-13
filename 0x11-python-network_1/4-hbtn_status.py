#!/usr/bin/python3

import requests

if __name__ == "__main__":
    retrieved_data = requests.get("https://intranet.hbtn.io/status")
    print('Body response:')
    print('\t- type:', type(retrieved_data.text))
    print('\t- content:', retrieved_data.text)
