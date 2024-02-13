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

