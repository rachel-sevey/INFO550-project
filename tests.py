import problems as prb
import algorithms as alg

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