'''
This file will contain implementations of each algorithm/agent type.
'''
import random

class RandomAgent:
  def __str__(self):
    return "Random Agent"
  def getMove(self, problem):
    moves = problem.getLegalMoves(problem.turn)
    return moves[random.randrange(len(moves))]
  
class BiggestPot: #Picks the biggest pot
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