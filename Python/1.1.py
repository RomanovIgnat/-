import datetime
import random
import sys


def get_coin_func():
    week_dict = {0: 5, 1: 10, 2: 7, 3: 5, 4: 0, 5: 4, 6: 0}

    def coin_func():

        if random.randint(1, 10) <= week_dict[datetime.date.today().weekday()]:
            print("решка", file=sys.stdout)
        else:
            print("орел", file=sys.stdout)

    return coin_func


coin = get_coin_func()
