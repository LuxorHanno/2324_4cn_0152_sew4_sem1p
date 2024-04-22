__author__ = "Hanno Postl"
__version__ = "1.7"
__status__ = "Finished"


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
    >>> print(Fraction(10,2))
    5
    >>> print(Fraction(-10,2))
    -5
    >>> print(Fraction(-1,2))
    -1/2
    >>> print(Fraction(1,-2))
    -1/2
    >>> print(Fraction(-1,-2))
    1/2
    >>> print(Fraction(-7,3))
    -2 1/3
    >>> f1+f2
    Fraction(3, 4)
    >>> f1-f2
    Fraction(1, 4)
    >>> f1*f2
    Fraction(1, 8)
    >>> f1/f2
    Fraction(2, 1)
    >>> f1//f2
    2
    >>> f1%f2
    Fraction(0, 1)
    >>> f1 == f2
    False
    >>> f1 != f2
    True
    >>> f1 < f2
    False
    >>> f1 <= f2
    False
    >>> f1 > f2
    True
    >>> f1 >= f2
    True
    >>> 1 + Fraction(1,2)
    Fraction(3, 2)
    >>> Fraction(1,2) + 1
    Fraction(3, 2)
    >>> 1 - Fraction(1,2)
    Fraction(1, 2)
    >>> Fraction(1,2) - 1
    Fraction(-1, 2)
    >>> 1 * Fraction(1,2)
    Fraction(1, 2)
    >>> Fraction(1,2) * 1
    Fraction(1, 2)
    >>> 1 / Fraction(1,2)
    Fraction(2, 1)
    >>> Fraction(1,2) / 1
    Fraction(1, 2)
    >>> 1 // Fraction(1,2)
    2
    >>> Fraction(1,2) // 1
    0
    >>> 1 % Fraction(1,2)
    Fraction(0, 1)
    >>> Fraction(1,2) % 1
    Fraction(1, 2)
    >>> Fraction(1,2) / Fraction(0,1)
    Traceback (most recent call last):
    ...
    ArithmeticError: Division durch 0 nicht erlaubt
    >>> Fraction(1,2) // Fraction(0,1)
    Traceback (most recent call last):
    ...
    ArithmeticError: Division durch 0 nicht erlaubt
    >>> Fraction(1,2) % Fraction(0,1)
    Traceback (most recent call last):
    ...
    ArithmeticError: Division durch 0 nicht erlaubt
    >>> 1.5 + Fraction(1,2)
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> Fraction(1,2) + 1.5
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> 1.5 - Fraction(1,2)
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> Fraction(1,2) - 1.5
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> 1.5 * Fraction(1,2)
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> Fraction(1,2) * 1.5
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> 1.5 / Fraction(1,2)
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> Fraction(1,2) / 1.5
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> 1.5 // Fraction(1,2)
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> Fraction(1,2) // 1.5
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> 1.5 % Fraction(1,2)
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> Fraction(1,2) % 1.5
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> Fraction(1,2) % 0
    Traceback (most recent call last):
    ...
    ArithmeticError: Division durch 0 nicht erlaubt
    >>> 5 % Fraction(0,2)
    Traceback (most recent call last):
    ...
    ArithmeticError: Division durch 0 nicht erlaubt
    >>> print(3 + 1 / (7 + Fraction(1, 15)))
    3 15/106
    >>> print(Fraction(-1,2) / Fraction(-1,-3))
    -1 1/2
    >>> print(Fraction(1))
    1
    >>> print(Fraction(1_000_000_000_000_000_001, 1_000_000_000_000_000_000) > 1)
    True
    """

    def __init__(self, zaehler=0, nenner=1):
        """Konstuktor"""

        if nenner == 0:
            raise ArithmeticError("Division durch 0 nicht erlaubt")
        self._numerator = zaehler
        self._denominator = nenner
        self.kuerzen()

    def kuerzen(self):
        """Kürzen"""
        ggt = (self.ggt(self.numerator, self.denominator))
        self.numerator //= ggt
        self.denominator //= ggt

    @staticmethod
    def ggt(a, b):
        while b != 0:
            c = a % b
            a, b = b, c
        return a

    def __str__(self):
        """String Methode"""
        ret = ""

        if self._numerator < 0:
            self.numerator *= -1
            ret = "-"

        if self.numerator >= self.denominator:
            if (self.numerator % self.denominator) == 0:
                return f"{ret}{self.numerator // self.denominator}"
            else:
                return f"{ret}{self.numerator // self.denominator} {self.numerator % self.denominator}/{self.denominator}"
        return f"{ret}{self.numerator}/{self.denominator}"

    def __repr__(self):
        """Repr Methode"""
        return f"Fraction({self.numerator}, {self.denominator})"

    def __float__(self):
        """Float Methode"""
        return self.numerator / self.denominator

    def __add__(self, other):
        """Addition"""
        if isinstance(other, int):
            return Fraction(self.numerator + other * self.denominator, self.denominator)
        elif isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)
        else:
            raise NotImplementedError

    def __radd__(self, other):
        """Addition"""
        if isinstance(other, int):
            return Fraction(other * self.denominator + self.numerator, self.denominator)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        """Subtraktion"""
        if isinstance(other, int):
            return Fraction(self.numerator - other * self.denominator, self.denominator)
        elif isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)
        else:
            raise NotImplementedError

    def __rsub__(self, other):
        """Subtraktion"""
        if isinstance(other, int):
            return Fraction(other * self.denominator - self.numerator, self.denominator)
        else:
            raise NotImplementedError

    def __mul__(self, other):
        """Multiplikation"""
        if isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)
        elif isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            raise NotImplementedError

    def __rmul__(self, other):
        """Multiplikation"""
        if isinstance(other, int):
            return Fraction(other * self.numerator, self.denominator)
        else:
            raise NotImplementedError

    def __truediv__(self, other):
        """Division"""
        if isinstance(other, int):
            return Fraction(self.numerator, self.denominator * other)
        elif isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        else:
            raise NotImplementedError

    def __rtruediv__(self, other):
        """Division"""
        if isinstance(other, int):
            return Fraction(other * self.denominator, self.numerator)
        else:
            raise NotImplementedError

    def __floordiv__(self, other):
        """Division"""
        if isinstance(other, int):
            return Fraction(self.numerator, self.denominator * other).__float__().__floor__()
        elif isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator).__float__().__floor__()
        else:
            raise NotImplementedError

    def __rfloordiv__(self, other):
        """Division"""
        if isinstance(other, int):
            return Fraction(other * self.denominator, self.numerator).__float__().__floor__()
        else:
            raise NotImplementedError

    def __mod__(self, other):
        """Modulo"""
        if isinstance(other, int):
            try:
                return Fraction(self.numerator % (self.denominator * other), self.denominator)
            except ZeroDivisionError:
                raise ArithmeticError("Division durch 0 nicht erlaubt")
        elif isinstance(other, Fraction):
            try:
                return Fraction((self.numerator * other.denominator) % (self.denominator * other.numerator),
                                self.denominator * other.denominator)
            except ZeroDivisionError:
                raise ArithmeticError("Division durch 0 nicht erlaubt")
        else:
            raise NotImplementedError

    def __rmod__(self, other):
        """Modulo"""
        if isinstance(other, int):
            try:
                return Fraction(other * self.denominator % self.numerator, self.denominator)
            except ZeroDivisionError:
                raise ArithmeticError("Division durch 0 nicht erlaubt")
        else:
            raise NotImplementedError

    def __eq__(self, other):
        """Gleichheit"""
        return self.numerator*other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        """Ungleichheit"""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Kleiner"""
        return self.numerator*other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        """Kleiner gleich"""
        return self.numerator*other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        """Größer"""
        return self.numerator*other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        """Größer gleich"""
        return self.numerator*other.denominator >= other.numerator * self.denominator

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
