"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner.

(picture from the problem)

How many such routes are there through a 20×20 grid?
"""

import math


def n_choose_r(n, r):
    assert n > r
    return math.factorial(n) // (math.factorial(n - r)**2)


if __name__ == '__main__':
    print(n_choose_r(40, 20))
