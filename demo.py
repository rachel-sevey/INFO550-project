import problems as prb
import algorithms as alg
import random

'''
This file will contain the code needed to run a demonstration of your project. 

For the progress report, it should contain code that shows a brief demonstration of random agents attempting to solve each problem. 

For the final report, it should contain code that shows a brief demonstration of each algorithm attempting to solve each problem. 

In both cases, to make sure we can grade these all in time, please ensure that each demonstration is just long enough to show some
meaningful behavior. If your problem is chess playing, for example, you might show 5 moves from each player, where one player uses one 
algorithm and one player uses another. If your problem is snake, you might show game long enough for the player to eat two apples or die
(whichever comes first).
'''

#Temporary disabling. 
#demoGame = prb.Game(prb.TicTacToe(),alg.RandomAgent(),alg.RandomAgent())
#demoGame.playGame()

#demoMancala = prb.Game(prb.Mancala(), alg.Minimax(),alg.RandomAgent())
#demoMancala.playGame()


score = []
games = 1000
tot_marbs_0 = 0
tot_marbs_1 = 0
player_0 = alg.Minimax()
player_1 = alg.MostMarbsToStore()
for i in range(int(games/2)):
    demoMancala = prb.Game(prb.Mancala(), player_0, player_1, verbose = False)
    winner, marbs_0, marbs_1 = demoMancala.playGame()
    score.append(winner)
    tot_marbs_0 += marbs_0
    tot_marbs_1 += marbs_1
    #Swap to remove first-player effect
    demoMancala_switch = prb.Game(prb.Mancala(), player_1, player_0, verbose = False)
    winner, marbs_0, marbs_1 = demoMancala_switch.playGame()
    if winner == -1: #Tie, no swap necessary
        score.append(winner)
    else:
        winner = abs(winner - 1)
        score.append(winner)
    tot_marbs_0 += marbs_1
    tot_marbs_1 += marbs_0

print(f"{player_0} won {score.count(0)} times")
print(f"{player_1} won {score.count(1)} times")
print(f"Agents tied {score.count(-1)} times")
print(f"Average marbles won by {player_0}: {tot_marbs_0 / games}")
print(f"Average marbles won by {player_1}: {tot_marbs_1 / games}")
