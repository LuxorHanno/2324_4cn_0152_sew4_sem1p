__author__ = "Hanno Postl"
__version__ = "1.0"
__status__ = "Finished"

def M(n):
    """
    Diese Funktion berechnet die Funktion M(n) aus der Aufgabenstellung.

    :param n: Eingabewert
    :return: Ausgabewert
    """
    if n <= 100:
        return M(M(n + 11))
    else:
        return n - 10