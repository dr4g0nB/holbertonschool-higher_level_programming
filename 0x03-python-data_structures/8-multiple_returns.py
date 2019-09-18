#!/usr/bin/python3
def multiple_returns(sentence):

    leng = len(sentence)

    if leng == 0:
        buff = None
    else:
        buff = sentence[0]
    return(leng, buff)
