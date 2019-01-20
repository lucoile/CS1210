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
from math import sqrt

######################################################################
# We'll represent vectors as lists of numbers; we'll define the vector
# class as a specialization of list so that we can handle
# normalization and dotproduct, while inheriting all of the usual list
# behaviors (so that, e.g., len(v) will work for v of type Vector).
#
# Th class constructor __init__() is a bit odd, because I want to show
# off an argument handling trick. We'll make the vector constructor
# simply invoke the inherited list constructor after grouping all the
# arguments given into a new list. This means Vector(1,2,3,4) will
# return a 4-element vector <1,2,3,4>, even though list(1,2,3,4) does
# not (the correct form is, e.g., list([1,2,3,4]), which returns
# [1,2,3,4]). This isn't necessarily a good idea, but grouping
# multiple remaining arguments with the *args construct is a good
# trick to know about.
class Vector(list):
    def __init__(self, *args):
        '''Constructor invokes list constructor on the collection of args given.'''
        list.__init__(self, list(args))

    def __repr__(self):
        '''Replace standard list brackets with angle brackets.'''
        S = list.__repr__(self)
        return('<{0}>'.format(S[1:len(S)-1]))

    # The scalar magnitude of a vector is the square root of the
    # individual elements squared. Think of it as the distance from
    # the n-dimensional origin to the tip of the n-dimensional
    # vector. Here, you will need to use the sqrt() function imported
    # from the math module.
    def magnitude(self):
        '''Returns scalar magnitude of self.'''
        return(sqrt(sum([ x**2 for x in self ])))

    # Normalizing a vector means changing its constituent values so
    # that it now represents a unit vector (a vector of length
    # 1). Only the magnitude of the vector (it's "length") changes;
    # the "direction" of the vector is unchanged. So the magnitude of
    # a normalized unit vector is always 1 (note: there may be some
    # slight round off numerical issues as shown in the handout).
    #
    # To normalize a vector, scale each element of the vector by 1
    # over the current magnitude of the vector. So normalizing a unit
    # vector makes no changes.
    #
    # Important: this method should change the object; it should
    # return True only when successful and False when it fails;
    # moreover it should not change the object if normalizing the
    # vector would fail.
    def normalize(self):
        '''Normalize self to unit magnitude. Returns True on success, False
           otherwise.'''
        m = self.magnitude()
        # Cannot divide by 0
        if m == 0:
            return(False)
        for i in range(len(self)):
            # Divide each element by the magnitude
            self[i] = self[i]/m
        return(True)

    # The dot product (sometimes called the scalar product) of two
    # vector is the sum of the pairwise product of the vector's
    # elements. So, for example, the dot product of <1, 2> and <3, 4>
    # is 11 (the sum of 1*3 and 2*4).
    #
    # Your implementation may profit from using zip() to "sew" to
    # lists together, element by element. So zip([1,2,3],[4,5,6])
    # yields a zip object that looks internally like [(1, 4), (2, 5),
    # (3, 6)].
    def dproduct(self, other):
        '''Returns the dot product of self and another vector.'''
        return(sum([ t[0]*t[1] for t in zip(self, other) ]))

    # The Euclidean distance between two vectors is the square root of
    # the sum of the squares of their element-by-element
    # differences. So, for example, the Euclidean distance between <1,
    # 2> and <3, 4> is about 2.8, while the Euclidean distance between
    # their normalized values is about 0.18.
    def edistance(self, other):
        '''Euclidean distance between two vectors.'''
        return(sqrt(sum([ (t[0]-t[1])**2 for t in zip(self, other)])))





