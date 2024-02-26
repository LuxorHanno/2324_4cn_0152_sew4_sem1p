__author__ = "Hanno Postl"
__version__ = "1.0"
__status__ = "under construction"

class spellcheck:
    def __init__(self, dictionary: str = "resources/de-en.txt"):
        """
        Konstruktor
        :param dictionary: Wörterbuch
        """
        self.__dictionary = dictionary

    def get_dictionary(self) -> str:
        """
        Diese Methode gibt das Wörterbuch zurück.

        :return: Wörterbuch
        """
        return self.__dictionary

    dictionary: str = property(get_dictionary)

    def read_all_words(self) -> set[str]:
        """
        Diese Methode liest das Wörterbuch ein und gibt eine Liste zurück.

        :return: Liste
        """
        with open(self.__dictionary, "r") as file:
            return set(file.read().split())

    def split_word(self, wort: str) -> list[tuple[str, str]]:
        """
        Diese Methode teilt das Wort in zwei Teile und gibt eine Liste zurück.


        >>> sc = spellcheck()
        >>> sc.split_word("abc")
        [('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '')]

        :param wort: Wort
        :return: Liste
        """
        return [(wort[:i], wort[i:]) for i in range(len(wort) + 1)]
