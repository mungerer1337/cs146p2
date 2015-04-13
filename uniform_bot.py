__author__ = 'Kevin Mike'

import random


def think(state, quip):

    random_move = random.choice(state.get_moves())

    return random_move
