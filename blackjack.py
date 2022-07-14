import argparse
import random

def run_simu(
    prob_win,
    prob_push,
    start_money,
    bet_unit,
    pocket_unit,
    ):

    table_money = start_money
    pocket_money = 0

    assert prob_win + prob_push < 1.0
    
    bet_amount = bet_unit
    while(table_money - bet_amount > 0):
        game_result = random.random()
        if(game_result < prob_win):
            table_money += bet_amount
            table_money -= pocket_unit
            pocket_money += pocket_unit
            bet_amount = bet_unit
        elif(game_result < prob_win + prob_push):
            pass # TODO
        else: # Lose game
            table_money -= bet_amount
            bet_amount *= 2 # double your bet    
    return pocket_money + table_money

def main(
        trials,
        prob_win,
        prob_push,
        start_money,
        bet_unit,
        pocket_unit,
    ):    
    sum_money_trials = 0
    for i in range(trials):
        sum_money_trials += run_simu(prob_win, prob_push, start_money, bet_unit, pocket_unit)

    avg_win = sum_money_trials * 1.0 / trials
    perc_start = avg_win / start_money
    print(
    """
    Num Trials:\t{trials}
    Avg win:\t{avg_win}
    % Start $:\t{perc_start}%
    """
        .format(trials=trials, avg_win=avg_win, perc_start=perc_start * 100)
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-t', '--trials', type=int,  default=10)
    parser.add_argument('-w', '--prob-win', type=float, default=0.425) 
    parser.add_argument('-p', '--prob-push', type=float, default=0.08) 
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
