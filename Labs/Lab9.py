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
# Write a meaningful comment here.
def superdigit(N):
    if len(str(N)) == 1:
        return(N)
    
    digits = [ int(d) for d in str(N) ]
    sumd = sum(digits)

    return(superdigit(sumd))
    

######################################################################
# Write a meaningful comment here.
#
# Note: you may elect to use the alternate signature supersum(N,S=0)
# if you prefer.
def supersum(N):
    if N == []:
        return(0)
    if type(N[0]) == int:
        return(N[0] + supersum(N[1:]))
    elif type(N[0]) == list:
        return(supersum(N[0]) + supersum(N[1:]))

######################################################################
# Write a meaningful comment here.
#
# Note: you may elect to use the alternate signature supersum(N,R=[])
# if you prefer.
def superlist(N, R=[]):
    if len(N) == 0:
        return(R)
    for i in N:
        if type(i) == int:
            R.append(i)
            N.remove(i)
        return(superlist(N, R))
            
        









