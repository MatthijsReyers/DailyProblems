#!/usr/bin/python3

# THE DAILY PROBLEM
# -------------------------------------------------------------------------------------
# Good morning! Here's your coding interview problem for today. This problem was asked 
# by Jane Street. cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the 
# first and last element of that pair. For example, car(cons(3, 4)) returns 3, 
# and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
#
# Implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def getfirst(a,b):
        return a
    return pair(getfirst)

def cdr(pair):
    def getlast(a,b):
        return b
    return pair(getlast)

if __name__ == '__main__':
    print('cdr(cons(3, 4)) returns:',car(cons(3, 4)))
    print('cdr(cons(3, 4)) returns:',cdr(cons(3, 4)))
