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
import string
from random import choices
from tkinter import *

class Boggle():
    # __init__() builds the data structure that holds the board, displays
    # the initial board, and sets up the game.
    def __init__(self, file='words.dat'):
        # Create a list of every letter in the alphabet.
        self.alpha = [ c for c in string.ascii_lowercase ]
        self.readData(file)
        # Create and populate a 5x5 board as a list of nested lists.
        self.board = [ [ ''.join((choices(self.alpha, [self.F[c] for c in self.alpha]))) for i in range(5) ] for j in range(5) ]
        self.soln = []
        # Create the window.
        self.window = Tk()
        self.window.title('Boggle')
        # Create a canvas within the window to draw on.
        self.canvas = Canvas(self.window, width = 100, height = 100, bg='white')
        self.canvas.pack()
        # Focus the mouse on the canvas.
        self.canvas.focus_set()
        # Bind different keys to their respective functions.
        self.canvas.bind("<Button-1>", self.extend)
        self.canvas.bind("<Button-2>", self.new)
        self.canvas.bind("<Button-3>", self.reset)
        # Display the initial state of the board.
        for i in range(5):
            for j in range(5):
                self.canvas.create_rectangle(i*20, j*20, (i+1)*20, (j+1)*20)
                self.canvas.create_text(i*20+10, j*20+10, text = self.board[i][j].upper())

    # readData() reads in a file of words and creates a letter frequency (self.F)
    # and a trie (self.T) using these words.
    def readData(self, file):
        fhand = open(file, 'r')
        # Create a list of every word in the file.
        words =  [ w.rstrip() for w in fhand ]
        # Create a dictionary with each letter and it's frequency among.
        # the words as its value
        self.F = { c:''.join(words).count(c)/len(''.join(words)) for c in self.alpha }
        self.T = dict()
        # The recursive helper function trie() helps build the trie of words.
        # The variable i is used for indexing and organization.
        def trie(D, w, word, i):
            # Once you reach the last letter, its value will be the word
            if i == 0:
                D[w[0]] = word
            else:
                # Create a dictionary with the letter if its not already in the trie
                if w[0] not in D:
                    D[w[0]] = {}
                    # Call trie again with a shadowed trie and the word without the first letter.
                    D[w[0]] = {w[1]:trie(D[w[0]], w[-i:], word, i-1)}
                else:
                    # If the letter is already in the current trie, update
                    # it with a new nested dictionary instead of overwriting it.
                    D[w[0]].update({w[1]:trie(D[w[0]], w[-i:], word, i-1)})
            return(D[w[0]])
        # Construct the trie one word at a time.
        for word in words:
            i = len(word)
            w = list(word)
            # Start off the helper function by doing the first letter for it.
            self.T[w[0]] = trie(self.T, w[-i:], word, i-1)
        # Cleanup the file.
        fhand.close()
        return()

    # ckSoln() takes a list of tuples that correspond to coordinates of letters
    # on the board. It uses these to check if a word can be made with this
    # succession of letters.
    def ckSoln(self, soln):
        # Create a list of the letters using the coordinates from soln.
        chars = [ self.board[i][j] for (i,j) in soln ]
        # A recursive helper function searches through the trie to find
        # if a word is possible with the letters from chars.
        def search(letters, trie, word):
            # If the letter doesn't exist in the trie, it will throw and error.
            # The try and except will catch this and return False.
            try:
                # Check if you got down to the last letter.
                if len(letters) == 1:
                    # If there is one letter left, return the trie shadowed to that letter.
                    return(trie[letters[0]])
                else:
                    # If there are more letters left, call search again but one
                    # level deeper into the trie.
                    return(search(letters[1:], trie[letters[0]], word))
            except:
                # Return False if there is no solution.
                return(False)
            
        return(search(chars, self.T, ''.join(chars)))
    
    def extend(self, event):
        # Calculate the row (i) and column (j) from the x and y of the event.
        i = event.x//20
        j = event.y//20

        # Add the event's coordinates to the solution.
        self.soln.append((i, j))
        # Check if the solution is viable.
        check = self.ckSoln(self.soln)
        # If there is a solution, draw a green circle
        if check:
            self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill='green')
            # If the viable solution is a word, print it and reset the solution.
            if type(check) == str:
                print(check)
                self.soln = []
        # If there isn't a viable solution, create a red circle.
        else:
            self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill='red')
        # Redraw the text ontop of the circle.
        self.canvas.create_text(i*20+10, j*20+10, text = self.board[i][j].upper())

        return()

    # new() repopulates the board with new letters and then redraws it.
    def new(self, event):
        # Repopulate the board.
        self.board = [ [ ''.join((choices(self.alpha, list(self.F.values())))) for i in range(5) ] for j in range(5) ]
        self.soln = []
        # Redraw the board.
        for i in range(5):
            for j in range(5):
                self.canvas.create_rectangle(i*20, j*20, (i+1)*20, (j+1)*20, fill = "white")
                self.canvas.create_text(i*20+10, j*20+10, text = self.board[i][j].upper())
        return()

    # reset() redraws the board.
    def reset(self, event):
        self.soln = []
        for i in range(5):
            for j in range(5):
                self.canvas.create_rectangle(i*20, j*20, (i+1)*20, (j+1)*20, fill = "white")
                self.canvas.create_text(i*20+10, j*20+10, text = self.board[i][j].upper())
        return()

    # solve() finds all the words on a board.
    def solve(self):
        # Create an empty list to store the words.
        solutions = []
        # A recursive helper functions searches the trie for words. The lambda
        # function tadd adds two tuples together into one.
        def search(soln, trie = self.T, tadd = lambda tx,ty: tuple([t[0]+t[1] for t in zip(tx,ty)])):
            # A dictionary where each direction is the key and its value is the
            # tuple that needs to be added to a tuple of coordinates to move
            # in that direction on the board.
            directions = {'right':(1,0), 'down':(0,1), 'left':(-1,0), 'up':(0,-1)}
            # Make sure the coordinates are on the board.
            if 0 < soln[0] > 4 or 0 < soln[1] > 4:
                    return()
            # Find the letter from the coordinates.
            letter = self.board[soln[0]][soln[1]]
            # Iterate through each direction.
            for drctn in directions:
                # Find the next coordinate by adding the direction to the current coordinate.
                nextSoln = tadd(soln, directions[drctn])
                # Assign newTrie to a shadowed version of the current trie. If this
                # fails, it means there is no solution and the loop needs to be broken.
                try:
                    newTrie = trie[letter]
                except:
                    break
                # If the shadowed trie is a string, it means its a word and that can be
                # appended to the list of solutions.
                if type(newTrie) == str:
                    solutions.append(trie[letter])
                    break
                else:
                # If the shadowed trie is not a word, its another trie and needs to
                # be searched deeper with the new solution.
                    search(nextSoln, newTrie)
            return()
        # Loop through every letter on the board and call search on it.
        for row in range(5):
            for col in range(5):
                search((row, col))
        # Return the list of solutions.
        return(solutions)






