from collections import Counter
from UE05.Caesar import Caesar


class Vigenere:

    def __init__(self, key: str = 'a'):
        """
        Konstruktor

        :param key: Schlüssel
        """
        self.__key = key

    def get_key(self) -> str:
        """
        Diese Methode gibt den Schlüssel zurück.

        :return: Schlüssel
        """
        return self.__key

    key: chr = property(get_key)

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        Diese Methode verschlüsselt einen Text mit dem Vigenere-Verfahren.

        >>> en = Vigenere()
        >>> en.encrypt("Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.", "StrengGeheim")
        'xkrrmpgkamuwgfgprzzzlvemzkcsfzkraefuinvvqaxgofikwke'



        :param plaintext: zu verschlüsselnder Text
        :param key: Schlüssel
        :return: Verschlüsselter Text
        """


    def decrypt(self, crypttext: str, key: str = None) -> str:
        """
        Diese Methode verschlüsselt einen Text mit dem Vigenere-Verfahren.

        >>> de = Vigenere()
        >>> de.decrypt("xkrrmpgkamuwgfgprzzzlvemzkcsfzkraefuinvvqaxgofikwke", "StrengGeheim")
        'franzjagtimkomplettverwahrlostentaxiquerdurchbayern'

        :param plaintext: zu verschlüsselnder Text
        :param key: Schlüssel
        :return: Verschlüsselter Text
        """




if __name__ == "__main__":
    pass
