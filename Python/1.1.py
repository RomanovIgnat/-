import datetime
import random
import sys


def get_coin_func():
    
    '''
    Возможны проблемы в работе функции в leep second, или при смене часовых поясов.
    '''
    
    week_dict = {0: 0.5, 1: 1, 2: 0.7, 3: 0.5, 4: 0, 5: 0.4, 6: 0}

    def coin_func():

        if random.random() <= week_dict[datetime.date.today().weekday()]:
            print("решка", file=sys.stdout)
        else:
            print("орел", file=sys.stdout)

    return coin_func


coin = get_coin_func()
