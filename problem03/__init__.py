# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def erats_sieve(upper_bound):
    num_dict = dict.fromkeys(range(2, upper_bound+1), True)
    for i in range(2, math.ceil(math.sqrt(upper_bound))):
        for j in range(i*i, upper_bound+1, i):
            num_dict[j] = False
    return [i for i in num_dict if num_dict[i] is True]


def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(int(i))
            n /= i

    if n > 2:
        factors.append(int(n))

    return factors


if __name__ == '__main__':
    print(prime_factors(600851475143)[-1])
