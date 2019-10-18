#!/usr/bin/python3
import sys
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    n_list = load_from_json_file('add_item.json')
except Exception:
    n_list = []

for trav in range(1, len(sys.argv)):
    n_list.append(sys.argv[trav])
save_to_json_file(n_list, 'add_item.json')
