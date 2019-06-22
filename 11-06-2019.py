#!/usr/bin/python3

# THE DAILY PROBLEM
# -------------------------------------------------------------------------------------
# This problem was recently asked by Google. Given a list of numbers and a number k, 
# return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


L = [10, 15, 3, 7]
K = 19

def FindSimple(l,k):
    for n in l:
        L2 = l.copy()
        L2.remove(n)
        for a in L2:
            if (n + a) == k: return True
    return False

def FindOnePass(l,k):
    for n in l:
        try: 
            l.index(k-n)
            return True
        except ValueError:
            pass
    return False

if __name__ == '__main__': print(FindOnePass(L,K))
