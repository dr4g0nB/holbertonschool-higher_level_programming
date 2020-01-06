#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response.
curl -sILf "$1" -X GET -w "%{http_code}" http://1ef36dcc94f7.38.hbtn-cod.io:5000
