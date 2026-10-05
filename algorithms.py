'''
This file will contain implementations of each algorithm/agent type.
'''
import random
import sys
import math

class RandomAgent:
  def __str__(self):
    return "Random Agent"
  def getMove(self, problem):
    moves = problem.getLegalMoves(problem.turn)
    return moves[random.randrange(len(moves))]
  
class BiggestPot: #Picks the biggest pot #TODO delete, trash
  def __str__(self):
      return "Biggest Pot"
  def getMove(self, problem):
    moves = problem.getLegalMoves(problem.turn)
    #print(f"Set of moves: {moves}")
    biggest_pot = 0
    loc = 0
    for m in moves:
      if problem.state[m] > biggest_pot:
        biggest_pot = problem.state[m]
        loc = m
        #print(f"Biggest pot: {biggest_pot}")
    return loc

class ExtraMove: #Prioritizes earning another turn, searches depth 1
  def __str__(self):
        return "Extra Move Agent"
  def getMove(self, problem):
    moves = problem.getLegalMoves(problem.turn)
    #print(f"Set of moves: {moves}")
    for m in moves:
      state_copy = problem.state.copy()
      state, extraMove, turn =  problem.getSuccessor(m, problem.turn, state_copy)
      if extraMove == True:
          #print(f"Extra move: {m}")
          return m
    return moves[random.randrange(len(moves))]


class MostMarbsToStore: #Counts the difference between the store after a move, so prioritizes capture of opponents marbs
  def __str__(self):
        return "Most Marbs to Store"
  def getMove(self, problem):
    moves = problem.getLegalMoves(problem.turn)
    store_diff = 0
    loc = None
    #print(f"Set of moves: {moves}")
    for m in moves:
      original_state = problem.state.copy()
      state_copy = problem.state.copy()
      state, extraMove, turn =  problem.getSuccessor(m, problem.turn, state_copy)
      if problem.turn == 0:
        marbs_moved = state[6] - original_state[6]
      if problem.turn == 1:
        marbs_moved = state[13] - original_state[13]
      if marbs_moved > store_diff:
        store_diff = marbs_moved
        loc = m
    if loc is not None:
        return loc
    return moves[random.randrange(len(moves))]

class Human:
    def __str__(self):
      return "Human"
    def getMove(self, problem):
      moves = problem.getLegalMoves(problem.turn)
      m = int(input("Please choose your move by entering an integer from 0 to 5: "))
      if m in moves:
        return m
      else: 
        print("Invalid, choosing a random move")
        return moves[random.randrange(len(moves))]

class Minimax:
    def __str__(self):
      return "Minimax"

    #TODO: sort out extra moves/turn counting
    #TODO: draw flowchart

    
    def getMove(self, problem):
      player_to_max = problem.turn #Figure out which side we're on (that we want to max)
      turn = problem.turn #Use this to take turns
      depth = 0
      return self.maxValue(problem, problem.state, player_to_max, turn, depth)

    def maxValue(self, problem, state, player_to_max, turn, depth):
      utility = -math.inf
      #Check terminal here?
      if problem.isTerminal(state) == True:
        winner = problem.getWinner(state)
        #See if we're the winner
        if winner == player_to_max:
           return math.inf
        elif winner == abs(player_to_max-1):
           return -math.inf
        else: return 0

      #Not terminal, check depth
      if depth >= 3:
        #run evaluation function TODO, this one is temporary
        if player_to_max == 0:
          utility = state[6] - state[13]
        else: #player is 1
          utility = state[13] - state[6]
        return utility

      #Not depth 5, run more recursion
      moves = problem.getLegalMoves(turn, state)
      results = []
      depth +=1
      for m in moves:
        state_copy = state.copy()
        state, extraMove, turn =  problem.getSuccessor(m, turn, state_copy)
        #Call min value? with new moves from current state and new depth?
        #UNLESS YOU GET AN EXTRA TURN, THEN CALL YOURSELF??
        results.append(self.minValue(problem, state, player_to_max, turn, depth))
      return max(results)
       
    def minValue(self, problem, state, player_to_max, turn, depth):
      utility = math.inf
      #Check terminal here?
      if problem.isTerminal(state) == True:
        winner = problem.getWinner(state)
        #See if the other player won
        if winner == player_to_max:
           return -math.inf
        elif winner == abs(player_to_max-1):
           return math.inf
        else: return 0

      #Not terminal, check depth
      if depth >= 3:
        #run evaluation function TODO, this one is temporary
        if player_to_max == 0:
          utility = state[13] - state[6] #Opposite the max function
        else: #player is 1
          utility = state[6] - state[13]
        return utility

      #Not depth 5, run more recursion
      moves = problem.getLegalMoves(turn, state)
      results = []
      for m in moves:
        state_copy = state.copy()
        state, extraMove, turn =  problem.getSuccessor(m, turn, state_copy)
        #Call min value? with new moves from current state and new depth?
        results.append(self.maxValue(problem, state, player_to_max, turn, depth))
      return min(results)