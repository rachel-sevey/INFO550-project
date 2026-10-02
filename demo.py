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

demoMancala = prb.Game(prb.Mancala(), alg.Human(),alg.MostMarbsToStore())
demoMancala.playGame()

'''
score = []
for i in range(5000):
    demoMancala = prb.Game(prb.Mancala(), alg.MostMarbsToStore(),alg.ExtraMove(), verbose = False)
    winner = demoMancala.playGame()
    score.append(winner)
    #Swap to remove first-player effect
    demoMancala_switch = prb.Game(prb.Mancala(), alg.ExtraMove(),alg.MostMarbsToStore(), verbose = False)
    winner = demoMancala_switch.playGame()
    if winner == -1:
        score.append(winner)
    else:
        winner = abs(winner - 1)
        score.append(winner)

print(f"Random Agent Zero won {score.count(0)} times")
print(f"Random Agent One won {score.count(1)} times")
print(f"Random Agents tied {score.count(-1)} times")
'''