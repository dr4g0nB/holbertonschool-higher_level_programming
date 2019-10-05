#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each of thaese chars . ? :

        Raise
        TypeError if text is not a string.
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    for trav in range(len(text)):
        print(text[trav], end="")
        if text[trav] == '.' or text[trav] == '?' or text[trav] == ':':
            print()
            print()
        elif text[trav] == 
            pass
