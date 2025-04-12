def strategy_round_3(opponent_id: int, my_history: dict[int, list[int]], opponents_history: dict[int, list[int]]) -> tuple[int, int]:

    if my_history[opponent_id]:
        return 0, random.choice(list(my_history.keys()))  # not cooperate with this guys
    return my_history[opponent_id][-1], random.choice(list(my_history.keys())) 
