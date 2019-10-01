#!/usr/bin/python3
import sys
def safe_function(fct, *args):

    try:
        eval(fct)
    except:
        sys.stderr.write("Exception: ")
        return None
    return
