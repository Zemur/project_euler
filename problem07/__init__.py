"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

from problem3 import erats_sieve
from timeit import Timer


def nth_prime(n):
    primes = []
    target = n * 2
    while len(primes) < n:
        primes = erats_sieve(target)
        # print(len(primes))
        # print(primes)
        target = target * 2
    return primes[n-1]


if __name__ == '__main__':
    nth = 10001
    t = Timer(lambda: nth_prime(nth))
    print(t.timeit(number=1))
    print(nth_prime(nth))
