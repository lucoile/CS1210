#!/usr/local/anaconda/bin/python
######################################################################
# Thomas Buffard
# A05
######################################################################

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.

######################################################################
# Replace "hawkid" in the singleton tuple in the function below with
# your own hawkid USING LOWER CASE CHARACTERS ONLY.
#
# ATTENTION: Your hawkid is your login name for ICON, it is not
# your student ID number. 
#
# Failure to correctly do so will result in a 0 grade.
######################################################################
def hawkid():
    return(("buffard",))

######################################################################
# Rounds up values in sequence S to the next variable of int r
def roundUp(S, r):
    return([x + (x % r) for x in S])

######################################################################
# Finds ratio of length of string S with no spaces to length of string S with spaces
def wordRatio(S):
    return(sum([len(x) for x in S.split()]) / len(S))

######################################################################
# Gives a dictionary with a word as the key and the amount of vowels as the value
def vcDict(S):
    return({x:sum([x.count(y) for y in ['a', 'e', 'i', 'o', 'u']]) for x in S.split()})

######################################################################
# Write a good comment here.
def allTriples(k):
##    [[[(x, y, z,) for z in range(k) if x > y > z] for y in range(k)] for x in range(k)]
    return(tuple([(x, y, z,) for x in range(k) for y in range(k) for z in range(k) if x > y > z ]))
