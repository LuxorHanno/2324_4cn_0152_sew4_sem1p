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

    def dist_n_tuple(self, text:str, laenge:int) -> set[tuple[str, int]]:
        """
        Überprüft alle Teilstrings aus text mit der gegebenen laenge und liefert ein Set
        mit den Abständen aller Wiederholungen der Teilstrings in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """
        return {(text[i:i + laenge], j - i) for i in range(len(text) - laenge + 1) for j in range(i + laenge, len(text)) if text[i:i + laenge] == text[j:j + laenge]}

    def dist_n_list(self, text:str, laenge:int) -> list[int]:
        """
        Wie dist_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach vorkommen.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2) == [2, 3, 5, 9, 11, 14]
        True
        >>> k.dist_n_list("heissajucheieinei", 3) == [9]
        True
        >>> k.dist_n_list("heissajucheieinei", 4) == []
        True
        """
        return sorted(set([j - i for i in range(len(text) - laenge + 1) for j in range(i + laenge, len(text)) if text[i:i + laenge] == text[j:j + laenge]]))