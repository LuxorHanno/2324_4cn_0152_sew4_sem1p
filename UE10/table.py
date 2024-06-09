"""
Author: Hanno Postl
Version: 1.1
Status: Finished
"""

import operator


def print_table(fun, title=""):
    """
    Druckt die Wahrheitstabelle der Funktion fun mit zwei boolean Operanden.

    :param fun: Die zu testende logische Funktion, die zwei boolean Werte als Argumente akzeptiert.
    :param title: Optionaler Titel für die Tabelle.
    """
    print(f"{title}")
    print("A     B     | Result")
    for a in [False, True]:
        for b in [False, True]:
            print(f"{a:<5} {b:<5} | {fun(a, b)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print_table(operator.or_, "NAND")
    print_table(operator.and_, "OR")
    print_table(operator.xor, "XOR")