"""
This script is used to crack the key for Caesar or Vigenere cipher encrypted messages.
It takes an input file, processes it and prints the most probable key.
The script supports both verbose and quiet modes.
"""

__author__ = "Hanno Postl"
__version__ = "1.3"
__status__ = "Finished"

import argparse
import os.path
import sys
sys.path.append('../UE05')

from Kasiski import Kasiski
from Caesar import Caesar

if __name__ == "__main__":
    # Argument parser for command line arguments
    parser = argparse.ArgumentParser(description="cvcrack - Caesar & Vigenere key cracker ")
    parser.add_argument("infile", help="File to be processed")
    parser.add_argument("-c", "--cipher", choices=["caesar", "c", "vigenere", "v"], default="c",
                        help="Cipher to be used")

    # Group for output mode arguments
    outputgroup = parser.add_mutually_exclusive_group()
    outputgroup.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    outputgroup.add_argument("-q", "--quit", action="store_true", help="Quiet mode, only returns the most probable key")

    # Parse the arguments
    args = parser.parse_args()

    result: str

    # Check if input file exists
    if not os.path.exists(args.infile):
        sys.stderr.write(args.infile + ": " + os.strerror(2))
    else:
        # Read the input file
        with open(args.infile, "r") as f:
            text: str = f.read()

        # If cipher is Caesar
        if args.cipher in ["c", "caesar"]:

            caesar = Caesar()
            res = caesar.crack(text)

            # If verbose mode is on
            if args.verbose:
                print(f"Cracking Caesar-encypted file {args.infile}: Key = {res[0]}")
            else:
                print(res[0])

        # If cipher is Vigenere
        elif args.cipher in ["v", "vigenere"]:

            kasisiki = Kasiski(text)
            len = kasisiki.ggt_count([kasisiki.dist_n_list(text, i) for i in range(3, 10)][0]).most_common(1)[0][0]
            res = kasisiki.crack_key(len)

            # If verbose mode is on
            if args.verbose:
                print(f"Cracking Vigenere-encypted file {args.infile}: Key = {res}")
            else:
                print(res)