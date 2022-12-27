#!/usr/bin/env python3

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
import timeit


def euclid_pythag_trips(perimeter):
    for m in range(2, int(math.sqrt(perimeter / 2))):
        if (perimeter / 2) % m == 0:
            if m % 2 == 0:
                d = m + 1
            else:
                d = m + 2
            while d < 2 * m and d <= perimeter / (2 * m):
                if perimeter / (2 * m) % d == 0 and math.gcd(d, m) == 1:
                    k = perimeter / 2 / (d * m)
                    n = d - m
                    a = k * (m**2-n**2)
                    b = 2 * k * n * m
                    c = k * (m**2+n**2)
                    print(f"d:{d}, k:{k}, m: {m}, n: {n}, a: {a}, b: {b}, c: {c}")
                    return a, b, c, a*b*c
                d += 2


def brute_force(perimeter):
    a = 1

    while a < perimeter / 3:
        b = a
        while b < perimeter / 2:
            c = perimeter - a - b
            # Visualisation of what the brute force calculates
            print(f"Testing if {a}^2 + {b}^2, = {c}^2")
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c, a * b * c
            b += 1
        a += 1


if __name__ == '__main__':
    # Brute Force
    t = timeit.Timer("brute_force(1000)", "from __main__ import brute_force")
    # print(brute_force(1000))

    # Numbers, numbers, numbers!!
    # t = timeit.Timer("euclid_pythag_trips(1000)", "from __main__ import euclid_pythag_trips")
    # print(euclid_pythag_trips(1000))

    # Timeit time
    print(t.timeit(number=10))

