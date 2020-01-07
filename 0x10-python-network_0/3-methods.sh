#!/bin/bash
# Takes in a URL and displays all HTTP methods
curl -sX OPTIONS *"$1"
