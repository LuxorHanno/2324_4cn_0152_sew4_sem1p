class Kasiski:

    def __init__(self, crypttext: str = ""):
        """
        Konstruktor

        :param crypttext: Geheimtext
        """
        self.__crypttext = crypttext

    def get_crypttext(self) -> str:
        """
        Diese Methode gibt den Crypttext zurück.

        :return: Crypttext
        """
        return self.__crypttext

    crypttext: str = property(get_crypttext)

    def allpos(self, text: str, teilstring: str) -> list[int]:
        """
        Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []
        """
        return [i for i in range(len(text)) if text[i:i + len(teilstring)] == teilstring]

    def alldist(self, text:str, teilstring:str) -> set[int]:
        """
        Berechnet die Abstände zwischen den Wiederholungen des Teilstrings im verschlüsselten Text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        {}
        """
        dist = {j - i for i in self.allpos(text, teilstring) for j in self.allpos(text, teilstring) if i < j}
        if dist == set():
            return {}

        return dist

