# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import itertools
import math


def largest_palindromic_number(lower, upper):
    n_combos = sorted([math.prod(i) for i in itertools.combinations([i for i in range(lower, upper)][::-1], 2)],
                      reverse=True)
    for i in n_combos:
        if str(i) == str(i)[::-1]:
            return i


if __name__ == '__main__':
    print(largest_palindromic_number(100, 1000))
