#!/usr/local/anaconda/bin/python
######################################################################
# YOUR NAME GOES HERE
# YOUR DISCUSSION SECTION (e.g., "A09") GOES HERE
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
# lt(a, b) returns True if a less than b 
def lt(a, b):
    return(a < b)

######################################################################
# gt(a, b) returns True is a is greater than b
def gt(a, b):
    return(a > b)

######################################################################
# shorter(a, b) returns True if len(a) < len(b) or if a and b are
# equal length and a < b
def shorter(a, b):
    return((len(a) < len(b)) or (len(a) == len(b) and a < b))

######################################################################
# longer(a, b) returns True if len(a) > len(b) or if a and b are
# equal length and a < b.
def longer(a, b):
    return((len(a) > len(b)) or (len(a) == len(b) and a < b))

######################################################################
# bestKofN(L, k, fn) returns a list of the ‘best’ k elements chosen
# from the list L, based on the definition of ‘best’ by function fn
def bestKofN(L, k, fn):
    # Finds the 'best' value of a list based on fn
    def findVal(L):
        i = 0
        newL = L
        # Compares how much 'better' each item of the list is
        while i < len(newL) - 1:
            # Swaps the items if the item is 'better' than the next one
            if (fn(newL[i], newL[i + 1])):
                newL[i], newL[i+1] = newL[i+1], newL[i]
            i = i + 1
        # Returns the 'best' item
        return(newL[-1])

    # Sorts the items, putting the 'best' item at beginning of the list
    # each iteration. Iterates through the minimum amount (k) of times.
    for i in range(k):
        m = L[i:].index(findVal(L[i:]))
        L[i],L[i+m] = L[i+m],L[i]
    return(L[:k])

######################################################################
# Selection sort as shown in lecture. This sort is O(N^2). 
def selsort(L):
    for i in range(len(L)-1):
        m = L[i:].index(min(L[i:]))
        L[i],L[i+m] = L[i+m],L[i]
    return(L)
