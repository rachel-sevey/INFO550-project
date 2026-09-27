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
  
class GreedyAgent: #Picks the biggest pot
  def __str__(self):
      return "Greedy Agent"
  def getMove(self, problem):
    moves = problem.getLegalMoves(problem.turn)
    biggest_pot = 0
    loc = 0
    for m in moves:
      if problem.state[m] > biggest_pot:
        biggest_pot = problem.state[m]
        loc = m
    return loc

class ExtraMove: #Prioritizes earning another turn, searches depth 1
  def __str__(self):
        return "mostToStore Agent"
  def getMove(self, problem):
    moves = problem.getLegalMoves(problem.turn)
    for m in moves:
      state, extraMove, turn =  problem.getSuccessor(m, problem.turn, problem.state)
      if extraMove == True:
          return m
    return moves[random.randrange(len(moves))]