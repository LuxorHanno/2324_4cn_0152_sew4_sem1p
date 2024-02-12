from collections import Counter

class Caesar:

    def __init__(self, key: chr = 'a'):
        """
        Konstruktor

        :param key: Schlüssel
        """
        self.__key = key



    def get_key(self) -> int:
        """
        Diese Methode gibt den Schlüssel zurück.

        :return: Schlüssel
        """
        return self.__key

    key: chr = property(get_key)



    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        Diese Methode verschlüsselt einen Text mit dem Caesar-Verfahren.

        >>> c = Caesar('A')
        >>> c.encrypt("ABC")
        'ABC'

        >>> c.encrypt("ABC", 'E')
        'EFG'


        :param plaintext: zu verschlüsselnder Text
        :param key: Schlüssel
        :return: Verschlüsselter Text
        """
        if key is None:
            key = self.__key

        key = key.lower()

        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                if plaintext[i].isupper():
                    plaintext = plaintext[:i] + chr((ord(plaintext[i]) + (ord(key)-97) - 65) % 26 + 65) + plaintext[i + 1:]
                else:
                    plaintext = plaintext[:i] + chr((ord(plaintext[i]) + (ord(key)-97) - 97) % 26 + 97) + plaintext[i + 1:]

        return plaintext

    def decrypt(self, plaintext: str, key=None) -> str:
        """
        Diese Methode entschlüsselt einen Text mit dem Caesar-Verfahren.

        >>> c = Caesar('C')
        >>> c.decrypt("DEF")
        'BCD'

        >>> c.decrypt("EFG", 'E')
        'ABC'

        :param plaintext: zu entschlüsselnder Text
        :param key: Schlüssel
        :return: Entschlüsselter Text
        """
        if key is None:
            key = self.__key
        return self.encrypt(plaintext, chr((ord('A') - ord(key)) % 26 + 97))

    @staticmethod
    def crack(plaintext: str, elements=1) -> list[str]:
        """
        Diese Methode entschlüsselt einen Text mit dem Caesar-Verfahren.

        >>> Caesar.crack("Hallo mein Name ist Grantelbart und mein Bart ist immer sehr grantig weil ich meinen grantingen Bart nicht genug ant grant medikamente gebe.", 1)
        ['R']

        :param plaintext: zu entschlüsselnder Text
        :param elements: Anzahl der zu erzeugenden Elemente
        :return: Liste mit den wahrscheinlichsten Schlüsseln
        """
        plaintext = plaintext.lower()
        counter = Counter(plaintext)
        most_common = counter.most_common(elements)
        return [chr((ord('e') - ord(e[0])) % 26 + 65) for e in most_common]

        





if __name__ == "__main__":
    pass
