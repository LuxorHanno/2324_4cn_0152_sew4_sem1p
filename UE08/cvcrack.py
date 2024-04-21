__author__ = "Hanno Postl"
__version__ = "1.1"
__status__ = "work in progress"

import argparse
import os
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="cvcrack - Caesar & Vigenere key cracker ")
    parser.add_argument("infile", help="File to be processed")
    parser.add_argument("-c", "--cipher", choices=["caesar", "c", "vigenere", "v"], default="c",
                        help="Zu verwendende Chiffre")

    outputgroup = parser.add_mutually_exclusive_group()
    outputgroup.add_argument("-v", "--verbose", action="store_true", help="Zeigt Infos an")
    outputgroup.add_argument("-q", "--quit", action="store_true", help="Liefert nur den wahrscheinlichsten Key zurück")

    args = parser.parse_args()

    if not os.path.exists(args.infile):
        sys.stderr.write(args.infile + ": " + os.strerror(2))
    else:

