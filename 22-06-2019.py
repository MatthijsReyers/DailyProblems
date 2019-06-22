#!/usr/bin/python3

# THE DAILY PROBLEM
# -------------------------------------------------------------------------------------
# Good morning! Here's your coding interview problem for today. This problem was asked
# by Facebook. Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
# count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka',
# and 'ak'. You can assume that the messages are decodable. For example, 
# '001' is not allowed.

def CountSolutions(msg):
    if len(msg) == 1: return 1
    elif int(msg[0]) < 3:
        if len(msg) == 2: 
            return 2
        else: 
            Solutions = CountSolutions(msg[2:])
            Solutions += CountSolutions(msg[1:])
            return Solutions
    else: return CountSolutions(msg[1:])
    
