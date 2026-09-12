'''
This file will contain your the code for your problems. 
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import random

class Game:
    def __init__(self, problem, pZero, pOne,verbose=True):
      self.problem = problem      
      self.players = [pZero,pOne]   
      self.verbose = verbose   
      if self.verbose:
         self.problem.showState()               
    def playGame(self):
      pCur=0
      while self.problem.isTerminal()==False:           
         move = self.players[pCur].getMove(self.problem)           
         self.problem.doMove(move)
         if self.verbose:
            self.problem.showState()
            print(f"Move {self.problem.ticks}:")
            print(self.problem.state)
         pCur = np.abs(pCur-1)
        
      wIndex = self.problem.getWinner()
      winner = self.players[wIndex]
      if wIndex == -1:
         winner = "DRAW"
      #display final state
      print(f"The Winner is {winner} ({wIndex})!")
      if self.verbose:
         self.problem.showState(4000)
      return wIndex
              
class TicTacToe:
   def __init__(self):
      self.state = np.zeros((3,3))      
      self.ticks=-1      
   def getLegalMoves(self, state=None):
      if state is None:
         state = self.state
      moves = []
      mark = 1
      if np.sum(np.abs(state))%2!=0:
         mark = -1       
      for i in range(state.shape[0]):
         for j in range(state.shape[1]):
            if state[i,j]==0:
               moves.append((mark,(i,j)))
      return moves             
   def getSuccessor(self, move, state):
      mark = move[0]
      loc = move[1]
      state[loc] = mark
      return state
   def doMove(self,move):
      self.state = self.getSuccessor(move,self.state)
      self.ticks+=1
   def isTerminal(self, state=None):
      if state is None:
         state = self.state         
      terminal = False
      val = self.evalTerminal(state)      
      if val ==0 and np.sum(np.abs(state))==9:
         terminal = True
      if val!=0:
         terminal = True
      return terminal
   def evalTerminal(self, state=None):
      if state is None:
         state = self.state
      val = 0      
      #pOne Wins
      pZeroWins = [np.max(np.sum(state,0))==3,np.max(np.sum(state,1))==3,np.trace(state)==3,np.trace(state[:,::-1])==3]
      pOneWins = [np.min(np.sum(state,0))==-3,np.min(np.sum(state,1))==-3,np.trace(state)==-3,np.trace(state[:,::-1])==-3]

      if np.any(pZeroWins):
         val = 1
      if np.any(pOneWins):
         val = -1
      return val
   def getWinner(self, state=None):
      if state is None:
         state = self.state
      val = self.evalTerminal(state)
      if val==1:
         return 0 
      elif val==-1:
         return 1
      else:
         return -1
   def showState(self, ms = 1000,state=None):
      if state is None:
         state = self.state  

      screen = np.zeros((150,150)).astype(np.uint8)         
      screen = cv2.line(screen,(0,49),(149,49),255) 
      screen = cv2.line(screen,(0,99),(149,99),255)
      screen = cv2.line(screen,(49,0),(49,149),255) 
      screen = cv2.line(screen,(99,0),(99,149),255)

      for i in range(state.shape[0]):
         for j in range(state.shape[1]):
            if state[i,j]==1:
               screen = cv2.line(screen,(5 +j*50,5+i*50),(44+j*50,44+i*50),255,2,cv2.LINE_AA) 
               screen = cv2.line(screen,(44+j*50,5+i*50),(5 +j*50,44+i*50),255,2,cv2.LINE_AA) 
            if state[i,j]==-1:
               screen = cv2.circle(screen, (25 +j*50,25+i*50), 20, 255, 2,cv2.LINE_AA) 
               
      cv2.imshow('TicTacToe',screen)
      cv2.waitKey(ms)

class Mancala:
   def __init__(self):
      #Array indices 6 and 13 represent the stores for player 0 and 1.
      self.state = np.array([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
      self.ticks = -1

   def getLegalMoves(self, state=None):
      if state is None:
         state = self.state
      moves = []
      #TODO: figure out who the current player is. 
      #TODO: Get the legal moves for the current player 
      return moves

   def getSuccessor(self, move, state):
      #TODO: Get a successor state after the given move is made
      #Don't actually apply the move, just plan a hypothetical action
      return state

   def doMove(self, move):
      #Apply the move the the board, update the move counter. I think this one is finished?
      self.state = self.getSuccessor(move,self.state)
      self.ticks+=1

   def isTerminal(self, state=None):
      if state is None:
         state = self.state         
      terminal = False
      val = self.evalTerminal(state)
      #TODO: Check val to see if the game is over
      #Val is set in the evalterminal function based on the who cleared their side
      return terminal

   def evalTerminal(self, state=None):
      if state is None:
         state = self.state
      val = 0
      #TODO: Who won the game? Do val 1 for player 0, -1 for player 1. Keep 0 for tie
      return val

   def getWinner(self, state=None):
      if state is None:
         state = self.state
      val = self.evalTerminal(state)
      #Change the win values to indicate which player won. -1 is a tie. 
      if val==1:
         return 0 
      elif val==-1:
         return 1
      else:
         return -1

   #TODO need to implement cv2
   def showState(self):
      random.seed(27)
      fig, ax = plt.subplots(figsize = (7,3))
      ax.set_xlim(-2, 7)
      ax.set_ylim(-1, 2)
      plt.axis('off')
      ax.set_aspect('equal')

      #Create board
      board = FancyBboxPatch((-1.4,-0.3), 7.8, 1.6, boxstyle = 'round', color = '#e8d9c4')
      left_store = FancyBboxPatch((-1.1,-0.1), 0.15, 1.2, boxstyle = 'round', color = '#d1bd9b')
      right_store = FancyBboxPatch((6,-0.1), 0.15, 1.2, boxstyle = 'round', color = '#d1bd9b')
      ax.add_patch(board)
      ax.add_patch(left_store)
      ax.add_patch(right_store)

      #Fill board with pits
      vert_spot = 0
      for pit_num in range(len(self.state)):
         if pit_num > 6: vert_spot = 1
         if pit_num > 6:
            #Opposite side pits go from right to left
            horz_spot = 12 - pit_num
         #Close side pits go from left to right
         else: horz_spot = pit_num
         #For all pits except the stores, draw...
         if (pit_num != 6 and pit_num != 13):
            print(f"Pit {pit_num} is at ({horz_spot}, {vert_spot}) with {self.state[pit_num]} marbles.")
            circ = Circle([horz_spot, vert_spot], radius = 0.4, color = '#d1bd9b')
            ax.add_patch(circ)

         #Fill pits and stores with marbles
         for m in range(self.state[pit_num]):
            random_x = random.uniform(-0.2, 0.2)
            random_y = random.uniform(-0.2, 0.2)
            marb = Circle([horz_spot + random_x, vert_spot + random_y], radius = 0.13, facecolor = "#2c659b", edgecolor = "#1a5083", alpha = 0.5)
            ax.add_patch(marb)

         #Add numbers of marbles
         ax.annotate(str(pit_num), [horz_spot, vert_spot], fontsize = 9)
      plt.savefig("test_board.png", bbox_inches = 'tight')
      plt.show(block = False)  
      plt.pause(3)
      plt.close()
      


   
      
