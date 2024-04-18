__author__ = "Hanno Postl"
__version__ = "1.8"
__status__ = "Finished"


class spellcheck:

    def __init__(self,
                 dictionary: str = r"C:\Users\hanno\PycharmProjects\2324_4cn_0152_sew4_sem1p\UE06\resources\de-en.txt"):
        """
        Konstruktor
        :param dictionary: Wörterbuch
        """
        self.__dictionary = dictionary
        self.__allWords = self.read_all_words()
        self.__allWords = {w.lower() for w in self.__allWords}

    def get_dictionary(self) -> str:
        """
        Diese Methode gibt das Wörterbuch zurück.

        :return: Wörterbuch
        """
        return self.__dictionary

    dictionary: str = property(get_dictionary)
    allWords: set[str] = property()

    def read_all_words(self, filename: str = None) -> set[str]:
        """
        Diese Methode liest das Wörterbuch ein und gibt eine Liste zurück.

        :return: Liste
        """
        if filename is None:
            filename = self.__dictionary

        with open(filename, "r") as file:
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

    def edit1(self, wort: str) -> set[str]:
        """
        Diese Methode gibt eine Menge von Wörtern zurück, die einen Editierabstand von 1 haben.


        :param wort: Wort
        :return: Menge
        """
        wort = wort.lower()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        splits = self.split_word(wort)
        deletes = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
        replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
        inserts = [a + c + b for a, b in splits for c in alphabet]
        return set(deletes + transposes + replaces + inserts)

    def edit1_good(self, wort: str, alle_woerter: list[str] = None) -> set[str]:
        """
        Diese Methode gibt eine Menge von Wörtern zurück, die einen Editierabstand von 1 haben und im Wörterbuch stehen.

        >>> sc = spellcheck()
        >>> sc.edit1_good("Alsuppe")
        {'aalsuppe'}

        :param wort: Wort
        :param alle_woerter: Liste
        :return: Menge
        """
        if alle_woerter is None:
            alle_woerter = self.__allWords

        return {word for word in self.edit1(wort) if word in alle_woerter}

    def edit2_good(self, wort: str, alle_woerter: list[str] = None) -> set[str]:
        """
        Diese Methode gibt eine Menge von Wörtern zurück, die einen Editierabstand von 2 haben und im Wörterbuch stehen.

        >>> sc = spellcheck()
        >>> sc.edit2_good("Umschaltmechansms") #zwei fehler
        {'umschaltmechanismus'}

        :param wort: Wort
        :param alle_woerter: Liste
        :return: Menge
        """
        if alle_woerter is None:
            alle_woerter = self.__allWords

        return {s
                for o in {word for word in self.edit1(wort)}
                for s in self.edit1(o)
                if s in alle_woerter}

    def correct(self, wort: str, alle_woerter: list[str] = None) -> set[str]:
        """
        Diese Methode gibt eine Menge von Wörtern zurück, die einen Editierabstand von 0, 1 oder 2
        haben und im Wörterbuch stehen.

        >>> sc = spellcheck()
        >>> sc.correct("Aalsuppe")
        {'aalsuppe'}
        >>> sc.correct("Alsuppe")
        {'aalsuppe'}
        >>> sorted(sc.correct("Alsupe"))
        ['aalsuppe', 'absude', 'alse', 'lupe']

        :param wort: Wort
        :param alle_woerter: Liste
        :return: Menge
        """
        if alle_woerter is None:
            alle_woerter = self.__allWords

        ret = {wort.lower() if wort.lower() in alle_woerter else None}  # Überprüfung, ob das Wort richtig ist
        if ret == {None}:
            ret = self.edit1_good(wort, alle_woerter)  # Überprüfung mit Edit-Distanz 1
            if not ret:
                ret = self.edit2_good(wort, alle_woerter)  # Überprüfung mit Edit-Distanz 2
        return ret
