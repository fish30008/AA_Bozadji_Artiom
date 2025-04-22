# AA_Bozadji_Artiom
Torunament 

### Short desccription of algorithm: 
This code defines a strategy for a decision-making game where it returns 1 (cooperate) or 0 (defect) based on patterns in the opponent's past actions and the player's own recent moves, aiming to detect and respond to consistent defection or specific behavior patterns. Additionaly this algorithm is always deffect and trying to trick the oponents algorithm with not random coopearations, based on other algorithms history.


### Round 2
Default Selection: The algorithm starts by setting the current opponent as the default next opponent, ensuring we always have a fallback option.
Scoring System: Each potential opponent receives a score based on multiple factors:

Initial Score Assignment:

New opponents (never played): Score of 50 (neutral)
Highly cooperative opponents (>70% cooperation rate): Score of 90
Opponents close to the "rejection-cooperation=21" condition: Score of 80
Other opponents: Score proportional to their cooperation rate


Deterministic Pseudo-Randomization:

Uses a formula: (score + (opp_id * 7 + round_total * 13) % 20) % 100
This creates variety without requiring a random library
Combines opponent ID and total rounds played across all opponents
Ensures we don't get stuck playing the same opponent repeatedly


Round Distribution Bonus:

Adds 10 points to opponents we've played less than 50 rounds with
Helps distribute rounds more evenly among opponents




Filtering Logic:

Excludes opponents we've already played the maximum 200 rounds with
This prevents exceeding the round limit constraint


Final Selection:

The opponent with the highest calculated score is selected
If all opponents have reached 200 rounds (unlikely), we default to the current opponent
