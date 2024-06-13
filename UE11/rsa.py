__author__ = "Hanno Postl"
__version__ = "1.0"
__status__ = "Finished"

import random
import miller_rabin


def ggt(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x


def generate_keys(number_of_bits):
    """
    Generates a pair of RSA keys.
    :param number_of_bits: The bit length of the keys.
    :return: A tuple containing the private and public key.
    >>> private, public = generate_keys(128)
    >>> d, n, _ = private
    >>> e, n, _ = public
    >>> for x in [239876563, 13123456789009876544657473, 12328753224, 123309876543954345678767654565456543412]:
    ...     c = pow(x, e, n)
    ...     y = pow(c, d, n)
    ...     assert x == y
    """
    n = 0
    while n.bit_length() <= number_of_bits:
        p, q = miller_rabin.generate_prime(number_of_bits // 2 + 1), miller_rabin.generate_prime(number_of_bits // 2)
        n = p * q
    phin = (p - 1) * (q - 1)

    def gen_encryptionkey(bit_length):
        while True:
            prime_candidate = random.getrandbits(bit_length)
            # Set the two most significant bits to 1 to ensure the number has the correct bit length
            prime_candidate |= (1 << (bit_length - 1)) | 1
            if ggt(prime_candidate, phin) == 1:
                return prime_candidate

    e = gen_encryptionkey(number_of_bits)
    d = pow(e, -1, phin)
    return (d, n, d.bit_length()), (e, n, e.bit_length())
