import argparse
import random
# import matplotlib.pyplot as plt

def run_simu(
    prob_win,
    prob_push,
    start_money,
    bet_unit,
    pocket_unit,
    ):

    table_money = start_money
    pocket_money = 0
    rounds_played = 0

    assert prob_win + prob_push < 1.0
    
    bet_amount = bet_unit
    while(table_money - bet_amount > 0):
        game_result = random.random()
        if(game_result < prob_win):
            table_money += bet_amount
            table_money -= min(pocket_unit, bet_amount)
            pocket_money += min(pocket_unit, bet_amount)
            bet_amount = bet_unit
        elif(game_result < prob_win + prob_push):
            pass # TODO
        else: # Lose game
            table_money -= bet_amount
            bet_amount *= 2 # double your bet    
        rounds_played += 1
        # if(table_money - bet_amount <= 0):
        #    bet_amount = bet_unit
    return pocket_money + table_money, rounds_played

def main(
        trials,
        prob_win,
        prob_push,
        start_money,
        bet_unit,
        pocket_unit,
    ):    
    sum_money_trials = 0
    moneys = []
    rounds = []
    for i in range(trials):
        money, rounds_played = run_simu(prob_win, prob_push, start_money, bet_unit, pocket_unit)
        sum_money_trials += money
        moneys.append(money)
        rounds.append(rounds_played)

    avg_win = sum(moneys) * 1.0 / trials
    perc_start = avg_win / start_money
    avg_rounds = sum(rounds) * 1.0 / trials
    money_per_round = sum([money * 1.0 / rounds[i] for i, money in enumerate(moneys)]) / trials
    print(
    """
    Num Trials:\t{trials}
    Avg win:\t{avg_win}
    % Start $:\t{perc_start}%
    Avg rounds:\t{avg_rounds}
    Money per round:\t{money_per_round}
    """
        .format(trials=trials, avg_win=avg_win, perc_start=perc_start * 100, avg_rounds=avg_rounds, money_per_round=money_per_round)
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-t', '--trials', type=int,  default=10)
    parser.add_argument('-w', '--prob-win', type=float, default=0.4222) 
    parser.add_argument('-p', '--prob-push', type=float, default=0.0848) 
    parser.add_argument('-s', '--start-money', type=float, default=8.0)
    parser.add_argument('-b', '--bet-unit', type=float, default=1.0) 
    parser.add_argument('-o', '--pocket-unit', type=float, default=1.0)
    args = parser.parse_args()
    main(args.trials, 
         args.prob_win,
         args.prob_push,
         args.start_money,
         args.bet_unit,
         args.pocket_unit)
