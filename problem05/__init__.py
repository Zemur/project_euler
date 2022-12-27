# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import problem3
import cProfile


def lcm(n):
    primes = problem3.erats_sieve(n)
    least_common_multiple = 1
    i = 0
    while i < len(primes) and primes[i] <= n:
        highest_powered_prime = primes[i]
        while highest_powered_prime**2 <= n:
            highest_powered_prime = highest_powered_prime**2
        least_common_multiple *= highest_powered_prime
        i += 1

    return least_common_multiple


if __name__ == '__main__':
    print(cProfile.run("lcm(20)"))
    print(lcm(20))
