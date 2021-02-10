"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from problem3 import erats_sieve


if __name__ == '__main__':
    print(sum(erats_sieve(2000000)))

