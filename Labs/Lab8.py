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
import csv
from math import sqrt, acos, degrees

######################################################################
# We'll represent vectors as lists of numbers; we'll define the vector
# class as a specialization of list so that we can handle
# normalization and dotproduct.

# This class is a bit odd, because I want to show off an argument
# handling trick. We'll make the vector constructor different from the
# list constructor by grouping all the arguments given into a new
# list. This means Vector(1,2,3,4) will return a 4-element vector
# <1,2,3,4>, even though list(1,2,3,4) does not (the correct form is
# list([1,2,3,4]), which returns [1,2,3,4]). This isn't necessarily a
# good idea, but grouping multiple remaining arguments with the *args
# construct is a good trick to know about.

# Also, I use zip() to "sew" to lists together, element by element, so
# zip([1,2,3],[4,5,6]) yields a zip object that looks internally like
# [(1, 4), (2, 5), (3, 6)]. To unzip: zip(*zip([1,2,3],[4,5,6])).
# Note zip() is handy for transposing matrices!
class Vector(list):
    def __init__(self, *args):
        '''Constructor invokes list constructor on the collection of args given.'''
        list.__init__(self, list(args))

    def __repr__(self):
        '''Replace standard list brackets with angle brackets.'''
        S = list.__repr__(self)
        return('<{0}>'.format(S[1:len(S)-1]))

    # Returns scalar magnitude of self rounded to 10 decimal places.
    def magnitude(self):
        '''Returns scalar magnitude of self rounded to 10 decimal places.'''
        return(round(sqrt(sum( [ val*val for val in self ])), 10))

    # Turns self into a unit vector; returns True on success, False on
    # failure (zero-length vector).
    def normalize(self):
        '''Normalize self to unit magnitude. Returns True on success, False
           otherwise.'''
        mag = self.magnitude()
        if mag == 0:
            return(False)
        for i in range(len(self)):
            self[i] = self[i]/mag
        return(True)

    # Modify to raise a TypeError (with message "Vector length
    # mismatch") when called on two vectors of different lengths.
    # Note use of zip() to simplify the code.
    def dproduct(self, other):
        '''Dot product of self and another vector.'''
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return(sum([ pair[0]*pair[1] for pair in zip(self,other) ]))

    # Modify to raise a TypeError (with message "Vector length
    # mismatch") when called on two vectors of different lengths.
    def edistance(self, other):
        '''Euclidean distance between two vectors.'''
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return(sqrt(sum([ pow(pair[0]-pair[1],2) for pair in zip(self,other) ])))

    # Returns a new Vector that is the element-by-element sum of the
    # two vectors self and other. As before, raise a TypeError when
    # attempting to add vectors of mismatched length.
    def add(self, other):
        '''Vector addition.'''
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return(Vector(*[ pair[0]+pair[1] for pair in zip(self,other) ]))

    # Returns a new Vector that is the element-by-element difference
    # of the two vectors self and other. As before, raise a TypeError
    # when attempting to subtract vectors of mismatched length.
    def sub(self, other):
        '''Vector subtraction.'''
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return(Vector(*[ pair[0]-pair[1] for pair in zip(self,other) ]))

    # Return the angle between unit vectors self and other expressed
    # in degrees using the cosine rule from the handout. Raise an
    # appropriate error if either vector is not a unit vector.
    def theta(self, other):
        '''Angle between two vectors.'''
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return(degrees(acos(self.dproduct(other)/(self.magnitude()*other.magnitude()))))
        






