"""
This script is used to encrypt or decrypt a message using Caesar or Vigenere cipher.
It takes an input file, processes it and writes the result to an output file.
The script supports both verbose and quiet modes.
It also supports both encryption and decryption modes.
The key for encryption/decryption is provided as an argument.
"""

__author__ = "Hanno Postl"
__version__ = "1.4"
__status__ = "Finished"

import argparse
import os.path
import sys
sys.path.append('../UE05')

from Caesar import Caesar
from Vigenere import Vigenere

if __name__ == "__main__":

    # Argument parser for command line arguments
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using Caesar or Vigenere cipher.")
    parser.add_argument("infile", help="File to be processed")
    parser.add_argument("outfile", nargs="?", help="Output file")
    parser.add_argument("-c", "--cipher", choices=["caesar", "c", "vigenere", "v"], default="caesar",
                        help="Cipher to be used")

    # Group for output mode arguments
    outputgroup = parser.add_mutually_exclusive_group()
    # Group for crypto mode arguments
    cryptogroup = parser.add_mutually_exclusive_group()

    outputgroup.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    outputgroup.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")
    cryptogroup.add_argument("-d", "--decrypt", action="store_true", help="Decrypt mode")
    cryptogroup.add_argument("-e", "--encrypt", action="store_true", help="Encrypt mode")
    parser.add_argument("-k", "--key", help="Encryption key")

    # Parse the arguments
    args = parser.parse_args()

    # Check if input file exists
    if not os.path.exists(args.infile):
        sys.stderr.write(args.infile + ": " + os.strerror(2))

    else:

        # Read the input file
        with open(args.infile, "r") as f:
            text: str = f.read()

        # If cipher is Caesar
        if args.cipher in ["caesar", "c"]:
            caesar = Caesar(args.key)

            # If mode is encrypt
            if args.encrypt:
                result: str = caesar.encrypt(text, args.key)
                if args.verbose:
                    print(
                        f"Encrypting Caesar with key = {args.key} from file {args.infile} into file {args.outfile}")

            # If mode is decrypt
            elif args.decrypt:
                result: str = caesar.decrypt(text, args.key)
                if args.verbose:
                    print(
                        f"Decrypting Caesar with key = {args.key} from file {args.infile} into file {args.outfile}")


        # If cipher is Vigenere
        elif args.cipher in ["vigenere", "v"]:
            vigenere = Vigenere(args.key)

            # If mode is encrypt
            if args.encrypt:
                result = vigenere.encrypt(text, args.key)
                if args.verbose:
                    print(
                        f"Encrypting Vigenere with key = {args.key} from file {args.infile} into file {args.outfile}")

            # If mode is decrypt
            elif args.decrypt:
                result = vigenere.decrypt(text, args.key)
                if args.verbose:
                    print(
                        f"Decrypting Vigenere with key = {args.key} from file {args.infile} into file {args.outfile}")

        # Write the result to the output file
        with open(args.outfile, "w") as f:
            f.write(result)