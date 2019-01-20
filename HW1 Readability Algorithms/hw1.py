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
# getBook(file) opens a file and reads in the contents, creating a string
# including only the relevant lines. Empty lines and lines that include
# only caps are deemed irrelevant content.
def getBook(file = 'wind.txt'):
    '''Returns a string of the contents of a file without blank lines and those containing all uppercase'''

    fhand = open(file, 'r')

    # Construct a list containing the lines of text we want
    # (those without all caps and not blank). Note that line.rstrip removes
    # all newline and return characters, making empty lines truely empty.
    # After creating the list of relevant lines, join them into a single
    # string of text and return that.
    return(' '.join([ line.rstrip() for line in fhand if line.rstrip() != []
              and not str(line).isupper() ]))
    # Cleanup
    fhand.close()

######################################################################
# Returns the inputed string text without possesives, parenthesis, commas, 
# colons, semicolons, hyphens and quotes and replaces all ? and !
# with . using .translate() and .replace()
def cleanup(text):
    '''Cleans up text input by removing extra punctuation and replacing ? and ! with .'''
    
    # Start by removing any 's in  text using .replace() Use .translate() to
    # replace items in text in the first argument with those in the second.
    # The third argument will remove any characters in text that are also
    # listed in the string.
    return(text.replace("'s", '').translate(text.maketrans(
        '?!-_', '..  ', """,'()";""")))

######################################################################
# Returns a list of lowercase words with no punctuation from a string text
def extractWords(text):
    '''Returns a list of all words from a string.'''
    # Import string to use .punctuation
    import string
    
    # Return a list of all words in text.
    # Remove punctuation from the words using .translate()
    # and make the words lowercase using .lower()
    words = [ word.translate(word.maketrans('', '', string.punctuation)).lower()
             for word in text.split() if len(word) > 0 ]
    return(words)

######################################################################
# extractSentences(text) seperates a string into a list where each
# sentence is an item, where each sentence is dermined by periods in the string
def extractSentences(text):
    '''Returns a list of seperated sentances in a text.'''
    sen, l = [], []

    # Iterate through each word in the text
    for word in text.split():
        # Add each word to its sentence if it is a word
        if (word != ''):
            sen.append(word)
        # If the word has a '.' in it, that indicates the end of a sentence,
        # and so the entire sentence is joined and appended to the list
        # of sentences. If it doesn't have a period, conitnue loop.
        if ('.' not in word):
            continue
        elif ('.' in word):
            l.append(' '.join(sen))
            sen = []
    # Add the final sentence to the list if the text doesn't end with a '.'
    if (sen != []):
        l.append(' '.join(sen))
    return(l)

######################################################################
# countSyllables(word) counts how many syllables are in a given word
def countSyllables(word):
    '''Returns the amount of syllables in a word'''
    # Make sure the word is a word. I was getting errors in wind.txt because
    # one of the words was just an empty string. Not sure why or how.
    if (len(word) == 0):
        return(0)
    
    # Remove any trailing E's or S's from the word
    if (word[-1] == 'e'):
        word = word.rstrip('e')
    elif (word[-1] == 's'):
        word = word.rstrip('s')
        
    # Create lowercase strings of consonants and vowels, excluting the
    # letter Y from both. This is because the Y can be a vowel or a consonant.
    cons = 'bcdfghjklmnpqrstvwxz'
    vowels = 'aeiou'
    # Make a list of the characters in word for future reference
    chars = [ x for x in word ]
    count = 0

    # Iterate through each letter in word, each time checking it to see if
    # it meets the conditions of a syllable.
    for i in range(len(word)):
        c = chars[i]

        # Count a vowel if the first letter starts with a vowel or Y
        if (i == 0 and (c in vowels or c == 'y')):
            count += 1
        # The letter is first checked if it is a Y proceeded by any
        # consonant (excluding another Y).
        elif (c == 'y' and chars[i - 1] in cons):
            count += 1
        # Then the letter is checked if it is a vowel proceeded by any
        # consonant, exlcuding Y because a Y and a vowel next to eachother
        # count as 1 vowel.
        elif (vowels.count(c) == 1 and chars[i - 1] in cons):
            count += 1
        # If the character is neither, move on to the next one.
        else:
            continue

    # Since every word must have at least 1 syllable, if the above loop
    # does not count any syllables (ex: he, a) it will add one.
    if (count == 0):
        count = 1
        
    return(count)
    
######################################################################
# Determines the Automated Readability Score of a text by using the average
# amount of words per sentence and average amount of characters per words.
def ars(text):
    '''Determines the Automated Readability Score of a text.'''
    words = extractWords(text)
    sens = extractSentences(text)

    # Calculate the average amount of words per sentence.
    wps = len(words) / len(sens)
    # Calculate the average amount of characters per word.
    cpw = len(''.join(words)) / len(words)
    
    ars = 4.71 * cpw + 0.5 * wps - 21.43
    return(ars)

######################################################################
# Determines the Flesch-Kincaid Readability Index of a text by using the
# average amount of words per sentence and average amount of syllables
# per words.
def fki(text):
    words = extractWords(text)
    sens = extractSentences(text)

    # Calculate the average amount of words per sentence.
    wps = len(words) / len(sens)
    # Calculate the average amount syllables per word.
    spw = sum([ countSyllables(word) for word in words ]) / len(words)
    
    fki = (0.39 * wps) + (11.8 * spw) - 15.59
    return(fki)

######################################################################
# Determines the Coleman-Liau Readability Index of a text by using the
# average amount of characters per 100 words and average amount of
# sentences per 100 words.
def cli(text):
    words = extractWords(text)
    sens = extractSentences(text)

    # Calculate the average amount of characters per 100 words
    cphw = len(''.join(words)) / len(words) * 100
    # Calculate the average amount of sentences per 100 words
    sphw = len(sens) / len(words) * 100

    cli = 0.0588 * cphw - 0.296 * sphw - 15.8
    
    return(cli)

######################################################################
# Reads in a book from a file and evaluates its readability. Returns
# None.
def evalBook(file='wind.txt'):
    text = cleanup(getBook(file))
    print("Evaluating {}:".format(file.upper()))
    print("  {:5.2f} Automated Readability Score".format(ars(text)))
    print("  {:5.2f} Flesch-Kincaid Index".format(fki(text)))
    print("  {:5.2f} Coleman-Liau Index".format(cli(text)))
