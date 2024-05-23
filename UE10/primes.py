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
def get_all_files(pathname):
    """Yield all files in pathname and all its subdirectories."""
    for name in os.listdir(pathname):
        full_path = os.path.join(pathname, name)
        if os.path.isdir(full_path):
            yield from get_all_files(full_path)
        else:
            yield full_path


if __name__ == "__main__":
    """
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
    """

    # Alle Dateien im aktuellen Verzeichnis und allen Unterverzeichnissen ausgeben
    for file in get_all_files(r"C:\Users\hanno\PycharmProjects\2324_4cn_0152_sew4_sem1p\UE09"):
        print(file)


    