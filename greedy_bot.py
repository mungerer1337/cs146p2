__author__ = 'Kevin Mike'


def think(state, quip):
    moves = state.get_moves()

    max_score = 0

    for move in moves:

        temp_state = state.copy()

        temp_state.apply_move(move)

        temp_score = temp_state.get_score()

        if temp_score > max_score:
            max_score = temp_score

            greedy_move = move

    return greedy_move