"""


"""

__author__ = "Hanno Postl"
__version__ = "1.0"
__status__ = "Production"


def is_palindrom(s: str):
    """
    >>> l = is_palindrom("regen");l
    False

    >>> l = is_palindrom("lagerregal");l
    True

    :param s: Eingabestring
    :return: Ausgabestring
    """
    # Entferne Leerzeichen und konvertiere zu Kleinbuchstaben
    resturnS = ''.join(e.lower() for e in s if e.isalnum())

    # Überprüfe, ob der bearbeitete String gleich ist, wenn umgekehrt
    return resturnS == resturnS[::-1]


"""eingabe = input("Gib einen String ein: ")

if is_palindrom(eingabe):
    print(f"{eingabe} ist ein Palindrom.")
else:
    print(f"{eingabe} ist kein Palindrom.")"""

pass
