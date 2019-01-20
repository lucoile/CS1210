#!/usr/bin/python3
# Alberto Maria Segre
#
# Copyright 2014, The University of Iowa.  All rights reserved.
# Permission is hereby given to use and reproduce this software 
# for non-profit educational purposes only.
from random import randint
from tkinter import *
from copy import deepcopy

class Othello ():
    def __init__(self, N=8):
        '''Initialize an NxN game board (force N even).'''
        self.size = N - N%2                  # Ensure N is even
        # The state of the game is saved in self.board.
        self.board = [ [ 0 for i in range(self.size) ] for j in range(self.size) ]
        self.board[self.size//2][self.size//2-1] = 1
        self.board[self.size//2-1][self.size//2] = 1
        self.board[self.size//2][self.size//2] = -1
        self.board[self.size//2-1][self.size//2-1] = -1
        # Player encoding; player 1 (O or white) and -1 (X or black)
        self.tokens = "X_O"
        self.tomove = 1                       # Who moves next?
        
    def __str__(self):
        '''Print out a human readable representation of the board.'''
        tokens = "X_O"				# Move to class?
        return('\n'.join([ '  '.join([ tokens[self.board[i][j]+1] for j in range(self.size) ]) for i in range(self.size) ]) + '\n')
    def __repr__(self):
        '''Print out a machine readable representation of the board.'''
        return('Othello: {}'.format(self.__dict__))

    def reset(self):
        '''Reset board to its initial state.'''
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = 0
        self.board[self.size//2][self.size//2-1] = 1
        self.board[self.size//2-1][self.size//2] = 1
        self.board[self.size//2][self.size//2] = -1
        self.board[self.size//2-1][self.size//2-1] = -1
        self.tomove = 1                       # Who moves next?
    def copy(self):
        '''Create a copy of the current board.'''
        clone=Othello(self.size)
        clone.board = deepcopy(self.board)
        clone.tokens = self.tokens
        clone.tomove = self.tomove
        return(clone)

    def nwhite(self):
        '''Count white (+1) pieces on board.'''
        return(sum([ sum([ x for x in row if x > 0]) for row in self.board]))
    def nblack(self):
        '''Count black (-1) pieces on board.'''
        return(-sum([ sum([ x for x in row if x < 0]) for row in self.board]))
    def score(self):
        '''Returns a positive number for white, negative for black, 0 for tie.'''
        return(sum([ sum([ x for x in row ]) for row in self.board ]))

    # Chip flipping mechanisms that query and alter state of the board.
    def countFlips(self, player, move, rinc, cinc):
        '''Returns number of chips that would flip in direction (rinc,cinc) from player's move.'''
        count = 0
        row, col = move[0] + rinc, move[1] + cinc
        while (row >= 0 and row < self.size and col >= 0 and col < self.size and self.board[row][col] == -1*player):
            count = count+1
            row, col = row+rinc, col+cinc
        if (row >= 0 and row < self.size and col >= 0 and col < self.size and self.board[row][col] == player):
            return(count)
        else:
            return(0)
    def countWeightedFlips(self, player, move, rinc, cinc):
        '''Returns number of chips that would flip in direction (rinc,cinc) from player's move,
	   weighted by the distance of the proposed move from its closest corner.'''
        def weight(self, move):
            # Distance in square geometry with diagonal moves allowed is simply
            # the largest component of the move.
            if max(move) < self.size//2:
                # Both coordinates are in upper left quadrant
                dist = max(move)
            elif min(move) >= self.size//2:
                # Both coordinates are in the upper right quadrant
                dist = self.size//2 - 1 - min(move)
            else:
                dist = max(min(move), self.size//2 - 1 - max(move))
            if dist%2 == 0:
                return(self.size - 2*dist)
            else:
                return(-1*self.size + 2*dist)
        # This part is just like countFlips()
        count = 0
        row, col = move[0] + rinc, move[1] + cinc
        while (row >= 0 and row < self.size and col >= 0 and col < self.size and self.board[row][col] == -1*player):
            count = count+1
            row, col = row+rinc, col+cinc
        if (row >= 0 and row < self.size and col >= 0 and col < self.size and self.board[row][col] == player):
            # Return the weighted move
            return(count*weight(self, move))
        else:
            return(0)
    def makeFlips(self, player, move, rinc, cinc):
        '''Actually flips the chips resulting from player's move. Assumes chips to flip.'''
        assert self.countFlips(player, move, rinc, cinc) > 0, "No chips to flip!"
        row, col = move[0] + rinc, move[1] + cinc
        while (row >= 0 and row < self.size and col >= 0 and col < self.size and self.board[row][col] == -1*player):
            self.board[row][col] = player
            row, col = row+rinc, col+cinc   

    # Methods to query and check board for legal moves, and to update state as result of a move.
    def checkLegalMove(self, player, move):
        '''Checks to see if a specified move is legal (i.e., open space and nonzero flips) or not.'''
        if self.board[move[0]][move[1]] != 0:
            return(False)
        for direction in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
            if self.countFlips(player, move, *direction):
                return(True)
        return(False)
    def findLegalMoves(self, player):
        '''Returns a list of all legal moves for player on current board.'''  
        return([ (x, y) for x in range(self.size) for y in range(self.size) if self.checkLegalMove(player, (x,y)) ])
    def applyMove(self, player, move):
        '''Makes move on behalf of player; uses assert.'''
        #assert self.checkLegalMove(player, move), "Not a legal move"
        if not self.checkLegalMove(player, move):
            print("Bad move {} for player {}!".format(move, player))
            exit()            
        self.board[move[0]][move[1]] = player
        for direction in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
            if self.countFlips(player, move, *direction) > 0:
                self.makeFlips(player, move, *direction)

    # Move selection functions. Return the next move for specified player or None.
    def selectMove0(self, player):
        '''Prompts the user to select a move from the legal moves.'''
        moves = self.findLegalMoves(player)
        if moves == []:
            return(None)
        print("{}: select a move:".format(self.tokens[player+1]))
        for i in range(len(moves)):
            print(' {}: {}, {}'.format(i, moves[i][0], moves[i][1]))
        move = len(moves)
        while (move >= len(moves) or move < 0):
            move = int(input("What move? "))
        return(moves[move])
    def selectMove1(self, player):
        '''Selects a random but still legal move to make.'''
        legal = self.findLegalMoves(player)
        if legal:
            # Careful! Remember randint is inclusive.
            return(legal[randint(0,len(legal)-1)])
        return(None)    
    def selectMove2(self, player):
        '''Selects legal move to maximize flips.'''
        legal = self.findLegalMoves(player)
        if legal:
            flips = [ sum([ self.countFlips(player, move, *direction)
                            for direction in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)) ])
                      for move in legal ]
            return(legal[flips.index(max(flips))])
        return(None)
    def selectMove3(self, player):
        '''Selects legal move to maximize flips, but breaks ties at random.'''
        legal = self.findLegalMoves(player)
        if legal:
            flips = [ sum([ self.countFlips(player, move, *direction)
                            for direction in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)) ])
                      for move in legal ]
            best = [ i for i in range(len(flips)) if flips[i] == max(flips) ]
            # Careful! Remember randint is inclusive.
            return(legal[best[randint(0,len(best)-1)]])
        return(None)
    def selectMove4(self, player):
        '''Selects legal move to maximize flips, but breaks ties at random.'''
        legal = self.findLegalMoves(player)
        if legal:
            flips = [ sum([ self.countWeightedFlips(player, move, *direction)
                            for direction in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)) ])
                      for move in legal ]
            best = [ i for i in range(len(flips)) if flips[i] == max(flips) ]
            # Careful! Remember randint is inclusive.
            return(legal[best[randint(0,len(best)-1)]])
        return(None)
    def selectMove5(self, player):
        '''Minimax procedure with 4-ply lookahead.'''
        def minimax(board, player, depth, maxdepth):
            if depth == maxdepth:
                # Terminal leaf: SBE is chip differential.
                return(player*board.score())
            # Create new boards representing each legal move.
            moves = board.findLegalMoves(player)
            # No legal moves is a loss.
            if len(moves) == 0:
                if depth == 0:
                    # Top level player is out of moves.
                    return(None)
                # Loss SBE is negative maximum chip differential.
                return(-(self.size*self.size))
            # List of board clones.
            results = [ board.copy() for move in moves ]
            # Apply the moves to the clones.
            for i in range(len(moves)):
                results[i].applyMove(results[i].tomove, moves[i])
                results[i].tomove = -1 * results[i].tomove
            # Collect the results.
            results = [ minimax(newboard, newboard.tomove, depth+1, maxdepth) for newboard in results ]
            if depth == 0:
                # Returns the move corresponding to maximum SBE result.
                return(moves[results.index(max(results))])
            # Returns maximum SBE result.
            return(-1 * max(results))
        # Invoke minimax with 4-ply lookahead (n.b., lookahead must be >= 1).
        return(minimax(self, player, 0, 4))

    # REPL game driver: white and black arguments are move selection
    # functions. If verbose is False, game play is silent.
    def play(self, white=lambda self, player: self.selectMove0(player), 
                   black=lambda self, player: self.selectMove1(player), 
                   verbose=True):
        '''Play the game using ASCII representations of the board.'''
        while self.findLegalMoves(self.tomove):
            # Display the current board.
            if verbose:
                print(self)
            # Fetch the next move.
            if self.tomove == 1:
                move = (white)(self, self.tomove)
            else:
                move = (black)(self, self.tomove)
            # If the move is None, you're done.
            if move is None:
                if verbose:
                    print("{} has no move remaining".format(self.tokens[self.tomove+1]))
                break
            if verbose:
                print("{} selects {}".format(self.tokens[self.tomove+1], str(move)))
            self.applyMove(self.tomove, move)
            self.tomove = -1*self.tomove
        score = self.score()
        if verbose:
            print(self)
            if score != 0:
                print("Congratulations, {}! You win!".format(self.tokens[int(score/abs(score))+1]))
            else:
                print("It's a draw!")
        return(score)

    # Evaluation of different automatic player strategies: it's a bake off!
    def tournament(self, N=100, white=lambda self, player: self.selectMove4(player), black=lambda self, player: self.selectMove3(player)):
        '''Play a silent tournament of N games and report the result.'''
        results = []
        for i in range(N):
            self.reset()
            results.append(self.play(white=white, black=black, verbose=False))
        score = sum([ 1 for r in results if r>0 ]) - sum([ 1 for r in results if r<0 ])
        print("{d} games: score={d}, average={5.2f} [min={d}, max={d}]".format(N, score, sum(results)/N, min(results), max(results)))
        return(score)

    # TK game driver: white and black arguments are move selection functions, one of which 
    # must be True to indicate the human player. Unlike the REPL interface, game play here 
    # is always displayed.
    def playTK(self, white=True, black=lambda self, player: self.selectMove5(player)):
        '''Play the game using the TKinter interface.'''
        # One of the players must be a human player.
        if white != True and black != True:
            print("One and only one player must be human.")
            return(None)

        # Adjust tokens attribute to reflect the name of the player instead.
        self.tokens = ('black', None, 'white')
        # We're going to cache the white/black players on local attributes of the object
        # so we can retrieve them from within the button callback. This might be cause
        # to go back and clean up the original play() method to use a similar scheme; not
        # that it's necessary, but it would be consistent to do so.
        self.white = white
        self.black = black

        # Initialize the interactive window.
        self.initTK()

        # If black is the human player, you must make one initial white move.
        if black == True:
            move = (white)(self, self.tomove)
            self.applyMove(self.tomove, move)
            self.tomove = -1*self.tomove

        # Ready to start accepting moves.
        self.window.mainloop()

    # Initialize the interactive window. 
    def initTK(self):      
        # Create a window object of type Tk.
        self.window = Tk()
        self.window.title('Othello')
        # Create a canvas within the window to draw on.
        self.canvas = Canvas(self.window, width = self.size*20, height = self.size*20, bg='white')
        self.canvas.pack()
        # Draw the grid on the canvas.
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i*20, j*20, (i+1)*20, (j+1)*20)
        # Bind left button click to a callback method.
        self.canvas.bind("<Button-1>", self.manageTK)
        self.canvas.bind("<Button-3>", self.newTK)
        # Focus the mouse on the canvas.
        self.canvas.focus_set()
        # Display the initial state of the board.
        self.updateTK()
        
    # Draws the board's current state on the TK window canvas.
    def updateTK(self):
        for i in range(self.size):
            for j in range(self.size):
                # We'll use black/white regular ovals to represent the chips.
                if self.board[i][j] > 0:
                    self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill='white')
                elif self.board[i][j] < 0:
                    self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill='black')
 
    # Event handler. Each click represents the user trying to make a move. If the
    # move is legal, make it, then execute a move from the other player before
    # waiting for the next click.
    def manageTK(self, event):
        row = event.x//20
        col = event.y//20
        if self.checkLegalMove(self.tomove, (row, col)):
            # Good to go. Apply the move. But first, clear the legal move
            # indicators just in case they are lit.
            self.clearLegalTK()
            self.applyMove(self.tomove, (row, col))
            self.tomove = -1*self.tomove
            # Update the interactive display.
            self.updateTK()

            # Now get a move from the other player.
            if self.tomove == 1:
                move = (self.white)(self, self.tomove)
            else:
                move = (self.black)(self, self.tomove)

            # No legal move falls through.
            if move is not None:
                # If player has a move, apply it.
                self.applyMove(self.tomove, move)
                self.tomove = -1*self.tomove
                # Update the interactive display.
                self.updateTK()

                # Check to make sure the human has a move left; 
                # if not, fall through.
                if self.findLegalMoves(self.tomove):
                    return

            # Either the autoplayer had no moves left, or the human
            # player's got nothing left after the autoplayer makes his
            # move. In any case, the game is over.
            score = self.score()
            if score != 0:
                print("Congratulations, {}! You win!".format(self.tokens[int(score/abs(score))+1]))
            else:
                print("It's a draw!")
        else:
            # Player clicked on an illegal move. Highlight legal moves.
            self.legalTK()

    # Start a new game.
    def newTK(self, event):
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i*20, j*20, (i+1)*20, (j+1)*20, fill='white')
        self.reset()
        self.updateTK()

    # Show the legal moves available.
    def legalTK(self):
        for move in self.findLegalMoves(self.tomove):
            self.canvas.create_oval(move[0]*20+8, move[1]*20+8, (move[0]+1)*20-8, (move[1]+1)*20-8, fill='red')
    # Clear the legal moves available.
    def clearLegalTK(self):
        for move in self.findLegalMoves(self.tomove):
            self.canvas.create_rectangle(move[0]*20, move[1]*20, (move[0]+1)*20, (move[1]+1)*20, fill='white')

# By default, play the standard game.
if __name__ == "__main__":
    Othello(8).playTK()
