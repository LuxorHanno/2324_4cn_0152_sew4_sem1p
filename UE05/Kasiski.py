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



