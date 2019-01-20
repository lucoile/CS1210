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
# A note about pass, which serves no real purpose:
#
# The pass is included in each function template simply to ensure the
# file as a whole can be loaded into Python even without definitions
# for the assigned functions. Without the pass, Python would generate
# a syntax error. You should replace the pass with your defitniion;
# leaving the pass in (often after a return(), which terminates
# execution of the function anyway) is meaningless, and points may be
# deducted if you continue to do so.

######################################################################
# isVowel(word, i) returns True if the ith letter of a word is a vowel,
# False if it is not based on the following rules:
#   1. 'aeio' is always a vowel
#   2. 'y' is a vowel unless it is the first character in a word
#   3. 'u' is a vowel except when it follows a 'g' or 'q'
#   4. 'w' is a vowel if it follows a vowel
def isVowel(word, i):
    '''Returns True or False depending on if the character is a vowel.'''
    c = word[i]

    # If statement checks if the character matches any of the vowel rules,
    # and return True of False accordingly.
    if (c in 'aeio'):
        return(True)
    elif (c != 0):
        if (c == 'y'):
            return(True)
        elif (c == 'u' and word[i - 1] not in 'gq'):
            return(True)
        elif (c == 'w' and word[i - 1] in 'aeiou'):
            return(True)
        else:
            return(False)
    else:
        return(False)
    
######################################################################
# countSyllables(word) counts the number of syllables in a word, depending
# on how many vowels are in the word. Ignores 'e', 'es', and 'ed' endings.
# Consecutive vowels count as one syllable.
def countSyllables(word):
    '''Counts the number of syllables in a word.'''
    # Return one syllable for words less than or equal to 3 characters.
    if len(word) <= 3:
        return(1)

    word = word.lower()
    length = len(word)
    count = 0

    # Ignore trailing 'e' if it isn't following an 'l'.
    if (word[-1] == 'e' and word[-2] != 'l'):
        length -= 1
    # Ignore any trailing 'es' and 'ed'
    elif ((word[-1] + word[-2]) == 'es' and (word[-1] + word[-2]) == 'ed'):
        length -= 2

    # Use isVowel to count the amount of vowels in the word.
    syllables = [ isVowel(word, i) for i in range(length) ]

    # Count up the amount of syllables, making sure to not count consecutive
    # vowels.
    for i in range(length):
        if (i == 0 and syllables[i] == True):
            count += 1
        elif (syllables[i] == True and syllables[i - 1] == False):
            count += 1
        else:
            continue
                    
    return(count)

######################################################################
# Homework 1 version of countSyllables() [for comparison].
#
# Returns the number of syllables in the specified word. Syllables are
# defined according to a few simple rules:
#   1. flush trailing -s and -e
#   2. each syllable starts with a vowel
#   3. y is a vowel when it follows a consonant
#   4. every word has at least one syllable
def HW1countSyllables(word):
    # Figure effective length of the word.
    length = len(word)
    if word[-1]=='s' or word[-1]=='e':
        length = length-1
    # Start at the beginning of the word and flush any leading consonants.
    i = 0
    while i < length and word[i].lower() not in 'aeiouy':
        i = i+1
    # Start counting syllables, starting with the first vowel or y (a
    # vowel in this context).
    s = 0
    while i < length:
        s = s+1
        # A y here is a vowel.
        if word[i].lower() == 'y':
            i = i+1
        # A y here is a consonant; skip other vowels.
        while i < length and word[i].lower() in 'aeiou':
            i = i+1
        # Skip consonants if there is any word left, stopping at first
        # vowel+y. Must skip at least one consonant to consider y a
        # vowel again.
        if i < length:
            i = i+1   # A non-y consonant.
        while i < length and word[i].lower() not in 'aeiouy':
            i = i+1
    return(max(s,1))
