#!/usr/local/anaconda/bin/python
# Thomas Buffard
# A05

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.

######################################################################
# PLEASE EDIT THIS FUNCTION REPLACING THE WORD 'hawkid' WITHIN
# THE QUOTATION MARKS WITH YOUR OWN HAWKID.
######################################################################
def hawkid():
    return(("01272222",))

######################################################################
# Convert Farenheit to Celsius
def f2c(t):
    return(5*(t-32)/9)

# Convert Celsius to Farenheit
def c2f(t):
    return(((9*t)/5)+32)

######################################################################
# START WORKING HERE
######################################################################
# Convert Celsius to Kelvin
def c2k(c):
    return(c-273.15)

# Convert Kelvin to Celsius
def k2c(k):
    return(k+273.15)

# Convert Kelvin to Farenheit
def k2f(k):
    return((9/5)*(k-273.15)+32)

# Convert Farenheit to Kelvin
def f2k(f):
    return((5/9)*(f-32)+273.15)

# Convert Delisle to Celsius
def d2c(d):
    return(100-(2/3)*d)

# Convert Celsius to Delisle
def c2d(c):
    return((3/2)*(100-c))

# Convert Delisle to Farenheit
def d2f(d):
    return(212-d*(6/5))

# Conert Farenheit to Delisle
def f2d(f):
    return((5/6)*(212-f))

# Convert Delisle to Kelvin
def d2k(d):
    return(373.15-(2/3)*d)

# Convert Kelvin to Delisle
def k2d(k):
    return((3/2)*(373.15-k))
