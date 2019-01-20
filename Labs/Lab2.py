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
# Gives min number in list max amount of times and max number in list min number of times
def minByMax(S):
    minimum = min(S)
    maximum = max(S)
    return(((minimum,) * maximum + (maximum,)* minimum))

######################################################################
# Replaces i through j in string S with string U
def insertString(S, i, j, U):
    listS = list(S)
    listS[i:j] = U
    
    return(''.join(listS))

######################################################################
# Gives all the unique items in a list
def findUnique(T):
    final = set(T)
    return(list(set(T)))

######################################################################
# Write a good comment here. inflateCenter([1,2,3], 5)
def inflateCenter(L, k):
    center = len(L) // 2
    for i in k:
        L.insert(center, 0.0)
    return(L)

