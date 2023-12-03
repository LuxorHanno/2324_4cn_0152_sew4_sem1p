__author__ = "Hanno Postl"
__version__ = "1.0"
__status__ = "Finished"


def collatz(n: int):
    """
    Diese Funktion führt einen Schritt der Collatzfolge aus.

    >>> l = collatz(4);l
    2

    >>> l = collatz(5);l
    16

    :param n: Eingabewert
    :return: Ausgabewert
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def collatz_sequence(n: int):
    """
    Diese Funktion führt die Collatzfolge aus.

    >>> l = collatz_sequence(4);l
    [4, 2, 1]

    >>> l = collatz_sequence(5);l
    [5, 16, 8, 4, 2, 1]

    >>> l = collatz_sequence(19);l
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    :param n: Eingabewert
    :return: Ausgabewert
    """
    # Erstelle eine Liste mit dem Startwert
    returnList = [n]

    # Führe die Collatzfolge aus, bis 1 erreicht ist
    while n != 1:
        n = collatz(n)
        returnList.append(n)

    return returnList


def longes_collatz_sequence(n: int) -> tuple[int, int]:
    """
    Diese Funktion findet die längste Collatzfolge mit einem Startwert unterhalb von n.

    >>> l = longes_collatz_sequence(100);l
    (97, 119)

    :param n: Eingabewert
    :return: Ausgabewert (Startwert, Länge der Collatzfolge)
    """

    # Initialisiere der Variable
    max_length_start: list[int, int] = [0, 0]

    # Iteriere über alle Startwerte
    for i in range(1, n):
        # Berechne die Collatzfolge
        sequence = collatz_sequence(i)

        # Speichere die Länge der Collatzfolge
        length = len(sequence)

        # Überprüfe, ob die Länge der aktuellen Collatzfolge größer als die bisher längste ist
        if length > max_length_start[1]:
            max_length_start = (i, length)

    return tuple(max_length_start)
