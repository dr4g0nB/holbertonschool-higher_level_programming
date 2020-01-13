#!/usr/bin/python3

from urllib import request

retrieved_data = request.urlopen("https://intranet.hbtn.io/status")
data = retrieved_data.read()
html = data.decode("UTF-8")
print('Body response:')
print('\t - type: {}'.format(type(html)))
print('\t - content:{}'.format(html))
