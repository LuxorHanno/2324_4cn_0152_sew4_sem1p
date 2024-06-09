"""
Author: Hanno Postl
Version: 1.4
Status: Finished
"""

import itertools
from time import time
import os


def primes():
    """Generator that yields prime numbers."""
    # Sieve of Eratosthenes
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1



if __name__ == "__main__":
    # Die ersten 100 Primzahlen ausgeben
    print(list(itertools.islice(primes(), 100)))

    # Alle Primzahlen bis 100.000 ausgeben
    for prime in primes():
        if prime > 100000:
            break
        print(prime, end=" ")

    print('\n')

    # Die 200.000. und 400.000. Primzahl bestimmen und die benötigte Zeit messen
    start_time = time()
    print(next(itertools.islice(primes(), 199999, None)))  # 200.000. Primzahl
    end_time = time()
    print(f"Time taken: {end_time - start_time}")

    start_time = time()
    print(next(itertools.islice(primes(), 399999, None)))  # 400.000. Primzahl
    end_time = time()
    print(f"Time taken: {end_time - start_time}")