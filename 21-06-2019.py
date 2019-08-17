#!/usr/bin/python3

import random

# THE DAILY PROBLEM
# -------------------------------------------------------------------------------------
# Good morning! Here's your coding interview problem for today. This problem was asked 
# by Square. Assume you have access to a function toss_biased() which returns 0 or 1 
# with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know 
# the bias of the coin.
#
# Write a function to simulate an unbiased coin toss.

def toss_biased():
    ran = random.randint(1,10)
    if ran > 4: return 1
    else: return 0

def toss_no_bias():
    result = (0,0)
    while (result == (0,0) or result == (1,1)):
        result = (toss_biased(),toss_biased())
    if result == (1,0): return 0
    else: return 1 # == (0,1)
