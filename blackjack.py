import argparse


def run_simu(
    prob_win,
    prob_push,
    start_money,
    bet_unit,
    pocket_unit,
    ):
    return start_money

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

    avg_win = sum_money_trials / trials
    print(
    """
    Num Trials:\t{trials}
    Avg win:\t{avg_win}
    """
        .format(trials=trials, avg_win=avg_win)
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--trials', dest='trials', action='store_const', const='trials', default=10)
    parser.add_argument('--prob-win', dest='prob_win', action='store_const', const='prob_win', default=0.45) 
    parser.add_argument('--prob-push', dest='prob_push', action='store_const', const='prob_push', default=0.0) 
    parser.add_argument('--start-money', dest='start_money', action='store_const', const='start_money', default=8)
    parser.add_argument('--bet-unit', dest='bet_unit', action='store_const', const='bet_unit', default=1) 
    parser.add_argument('--pocket-unit', dest='pocket_unit', action='store_const', const='pocket_unit', default=1)
    args = parser.parse_args()
    main(args.trials, 
         args.prob_win,
         args.prob_push,
         args.start_money,
         args.bet_unit,
         args.pocket_unit)
