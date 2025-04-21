def strategy_round_(opponent_id: int, my_history: dict[int, list[int]], opponents_history: dict[int, list[int]]) -> tuple[int, int]:
        
    try:
        my_moves = my_history[opponent_id]
        opponent_moves = opponents_history[opponent_id]
        move = 0  
        if not opponent_moves:
            move = 0
        else:
            cooperation, rejection = 0, 0
            for i in opponent_moves:
                if i == 0:
                    rejection += 1
                else:
                    cooperation += 1
            if len(my_moves) >= 2 and my_moves[-2:] == [1, 0]:
                move = 0
            elif 95 <= len(opponent_moves) < 100:
                move = 0
            elif cooperation == 0 and rejection < 25:
                move = 1
            elif rejection - cooperation == 21:
                move = 1
            elif len(opponent_moves) >= 10 and all(move == 0 for move in opponent_moves[-10:]):
                move = 1
            else:
                move = 0
        
        next_opponent_candidates = []
        
        for opp_id in my_history:
            if len(my_history[opp_id]) >= 200:
                continue
                
            opp_moves = opponents_history[opp_id]
            if not opp_moves:
                next_opponent_candidates.append(opp_id)
            else:
                coop_rate = sum(opp_moves) / len(opp_moves) if opp_moves else 0
                
    
                if coop_rate > 0.7:
                    next_opponent_candidates.append(opp_id)
                    next_opponent_candidates.append(opp_id)  
    
                elif opp_moves and (sum(1 for m in opp_moves if m == 0) - sum(1 for m in opp_moves if m == 1)) in [20, 21, 22]:
                    next_opponent_candidates.append(opp_id)
                    next_opponent_candidates.append(opp_id) 
                else:
                    next_opponent_candidates.append(opp_id)
        
        # If no eligible opponents, use current opponent
        if not next_opponent_candidates:
            next_opponent = opponent_id
        else:
            next_opponent = opponent_id + 1
    except:
        return 0, idk
    
    return move, next_opponent
