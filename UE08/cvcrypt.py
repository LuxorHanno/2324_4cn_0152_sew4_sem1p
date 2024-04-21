__author__ = "Hanno Postl"
__version__ = "1.4"
__status__ = "Finished"

import argparse
import os.path
import sys

from Caesar import Caesar
from Vigenere import Vigenere

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using Caesar or Vigenere cipher.")
    parser.add_argument("infile", help="File to be processed")
    parser.add_argument("outfile", nargs="?", help="Output file")
    parser.add_argument("-c", "--cipher", choices=["caesar", "c", "vigenere", "v"], default="caesar",
                        help="Cipher to be used")

    outputgroup = parser.add_mutually_exclusive_group()
    cryptogroup = parser.add_mutually_exclusive_group()

    outputgroup.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    outputgroup.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")
    cryptogroup.add_argument("-d", "--decrypt", action="store_true", help="Decrypt mode")
    cryptogroup.add_argument("-e", "--encrypt", action="store_true", help="Encrypt mode")
    parser.add_argument("-k", "--key", help="Encryption key")

    args = parser.parse_args()

    if not os.path.exists(args.infile):
        sys.stderr.write(args.infile + ": " + os.strerror(2))

    else:

        with open(args.infile, "r") as f:
            text: str = f.read()

        if args.cipher in ["caesar", "c"]:
            caesar = Caesar(args.key)

            if args.encrypt:
                result: str = caesar.encrypt(text, args.key)
                if args.verbose:
                    print(
                        f"Encrypting Caesar with key = {args.key} from file {args.infile} into file {args.outfile}")

            elif args.decrypt:
                result: str = caesar.decrypt(text, args.key)
                if args.verbose:
                    print(
                        f"Decrypting Caesar with key = {args.key} from file {args.infile} into file {args.outfile}")


        elif args.cipher in ["vigenere", "v"]:
            vigenere = Vigenere(args.key)

            if args.encrypt:
                result = vigenere.encrypt(text, args.key)
                if args.verbose:
                    print(
                        f"Encrypting Vigenere with key = {args.key} from file {args.infile} into file {args.outfile}")

            elif args.decrypt:
                result = vigenere.decrypt(text, args.key)
                if args.verbose:
                    print(
                        f"Decrypting Vigenere with key = {args.key} from file {args.infile} into file {args.outfile}")

        with open(args.outfile, "w") as f:
            f.write(result)
