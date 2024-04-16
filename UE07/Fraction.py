__author__ = "Hanno Postl"
__version__ = "1.0"
__status__ = "work in progress"


class Fraction:
    """ Klasse für Bruchzahlen
    >>> f1 = Fraction(1,2)
    >>> f1 # __repr__
    Fraction(1, 2)
    >>> print(f1) # __str__
    1/2
    >>> f2 = Fraction(1,4)
    >>> print(f2)
    1/4
    >>> f1+f2
    Fraction(3, 4)
    """

    def __init__(self, zaehler=0, nenner=1):
        """Konstuktor"""
        self._numerator = zaehler
        self._denominator = nenner
        self.kuerzen()

    def kuerzen(self):
        """Kürzen"""
        ggt = (self.ggt(self.numerator, self.denominator))
        self.numerator //= ggt
        self.denominator //= ggt

    @staticmethod
    def ggt(a, b):  # Funktion für den GGT
        while b != 0:
            c = a % b
            a, b = b, c
        return a

    def __str__(self):
        """String Methode"""
        if self.numerator > self.denominator:
            return f"{self.numerator // self.denominator} {self.numerator % self.denominator}/{self.denominator}"
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """Repr Methode"""
        return f"Fraction({self.numerator}, {self.denominator})"

    def __float__(self):
        """Float Methode"""
        return self.numerator / self.denominator

    def __add__(self, other):
        """Addition"""
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        """Subtraktion"""
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        """Multiplikation"""
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        """Division"""
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __floordiv__(self, other):
        """Division"""
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator).__float__().__floor__()

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @denominator.setter
    def denominator(self, value):
        self._denominator = value


if __name__ == "__main__":
    f1 = Fraction(7, 6)
    f2 = Fraction(5, 8)
    print(f1)
    print(f2)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 / f2)
    print(f1 // f2)
