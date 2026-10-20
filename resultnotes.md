## For keeping track of matchups while creating evaluation function candidates
---
For each run, I'm alternating the starting player, as that conveys an advantage. Player Zero is the initial starting player
Player Zero     Player One       Runs       P0Wins     P1Wins      Ties
Random          Random           10000      4674       4726        600       
BiggestPot      RandomAgent      10000      4783       4556        661   
ExtraMove       RandomAgent      10000      7925       1667        408      
ExtraMove       BiggestPot       10000      8602       1061        337
MostMarbsToStore Random          10000      9469       400         131
MostMarbsToStore ExtraMove       10000      7791       1789        420
Minimax2        MostMarbs        1000       1000       0           0            (Avg ratio of marbles: 31.33:16.67)
Minimax3        MostMarbs        1000       1000       0           0            (Avg ratio of marbles: 30.39:17.61)

#Minimax2 is depth 2 and uses an evaluation function that counts the diff between stores.
#Minimax3 is depth 3 and uses an evaluation function that counts the diff between stores.
