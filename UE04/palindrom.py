__author__ = "Hanno Postl"
__version__ = "1.2"
__status__ = "Finished"


def is_palindrom(s: str):
    """
    Diese Methode überprüft, ob ein String ein Palindrom ist.
    Dabei beachtet sie nicht die Groß- und Kleinschreibung und auch keine Satzzeichen.

    >>> l = is_palindrom("regen");l
    False

    >>> l = is_palindrom("lager!regal");l
    True

    :param s: Eingabestring
    :return: Ausgabestring
    """

    # Überprüfe, ob der bearbeitete String gleich ist, wenn umgekehrt
    return str(s) == str(s)[::-1]


def is_palindrom_sentence(s: str):
    """
    Diese Methode überprüft, ob ein String ein Palindrom ist.
    Dabei beachtet sie nicht die Groß- und Kleinschreibung und auch keine Satzzeichen.

    >>> l = is_palindrom_sentence("Regen kann auch schweben");l
    False

    >>> l = is_palindrom_sentence("Oh, Cello! Voll Echo!");l
    True

    :param s: Eingabestring
    :return: Ausgabestring
    """
    # Entferne Leerzeichen und konvertiere zu Kleinbuchstaben
    resturnS = ''.join(e.lower() for e in s if e.isalnum())

    # Überprüfe, ob der bearbeitete String gleich ist, wenn umgekehrt
    return resturnS == resturnS[::-1]


def palindrom_product(x):
    """
    Diese Methode berechnet das größte Palindrom, das das Produkt zweier dreistelliger Zahlen ist.
    Das Produkt muss kleiner als x sein.

    >>> l = palindrom_product(23440);l
    23432

    >>> l = palindrom_product(23400);l
    23232

    >>> l = palindrom_product(100000);l
    99999

    :param x: Maximalwert des Produktes
    :return: Größte Palindromzahl
    """

    max_palindrome = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if product < x and str(product) == str(product)[::-1] and product > max_palindrome:
                max_palindrome = product

    return max_palindrome

def to_base(number, base):
    """
    Diese Methode konvertiert eine Zahl in ein anderes Zahlensystem.



    >>> l = to_base(10, 16);l
    'A'

    :param number: Nummer, die konvertiert werden soll
    :param base: Zielsystem
    :return: konvertierte Zahl
    """

    if number == 0:
        return '0'

    hex_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while number > 0:
        remainder = number % base
        result = hex_chars[remainder] + result if base == 16 else str(remainder) + result
        number //= base

    return result


def get_dec_hex_palindrom(x):
    """
    Diese Methode berechnet das größte Palindrom, das sowohl in Dezimal- als auch in Hexadezimaldarstellung ein Palindrom ist.
    Die Dezimalausgabe muss kleiner als x sein.

    >>> l = get_dec_hex_palindrom(10000);l
    '3003 (dezimal) = BBB (hexadezimal)'

    >>> l = get_dec_hex_palindrom(1000);l
    '979 (dezimal) = 3D3 (hexadezimal)'

    >>> l = get_dec_hex_palindrom(100);l
    '11 (dezimal) = B (hexadezimal)'

    :param x: Maximalwert der Dezimalausgabe
    :return: Größte Palindromzahl in Dezimal- und Hexadezimaldarstellung
    """
    max_palindrome = 0

    for i in range(x - 1, 0, -1):
        # Überprüfen, ob sowohl die Dezimal- als auch die Hexadezimalrepräsentation ein Palindrom ist
        decimal_palindrome = is_palindrom(str(i))
        hex_palindrome = is_palindrom(to_base(i, 16))

        if decimal_palindrome and hex_palindrome:
            max_palindrome = i
            break

    return f"{max_palindrome} (dezimal) = {to_base(max_palindrome, 16)} (hexadezimal)"
