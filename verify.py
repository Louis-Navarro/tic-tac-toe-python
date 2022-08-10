import numpy as np


def verify_symbol(grid, symbol):
    if ((grid == symbol).sum(axis=0) == 3).any():
        return True

    elif ((grid.T == symbol).sum(axis=0) == 3).any():
        return True

    elif ((grid.diagonal() == symbol).sum() == 3):
        return True

    elif ((np.fliplr(grid).diagonal() == symbol).sum() == 3):
        return True

    return False


def verify(grid):
    if verify_symbol(grid, 'X'):
        return 'X'

    elif verify_symbol(grid, 'O'):
        return 'O'

    elif not np.argwhere(grid == '-').size:
        return 'Tie'

    return None
