#!/bin/bash
# Takes in a URL and displays all HTTP methods
curl -s OPTIONS *"$1"
