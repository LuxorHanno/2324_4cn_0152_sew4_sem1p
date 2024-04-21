__author__ = "Hanno Postl"
__version__ = "1.2"
__status__ = "Finished"

import argparse
import os.path
import sys
sys.path.append('../UE05')


from Kasiski import Kasiski
from Caesar import Caesar

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="cvcrack - Caesar & Vigenere key cracker ")
    parser.add_argument("infile", help="File to be processed")
    parser.add_argument("-c", "--cipher", choices=["caesar", "c", "vigenere", "v"], default="c",
                        help="Zu verwendende Chiffre")

    outputgroup = parser.add_mutually_exclusive_group()
    outputgroup.add_argument("-v", "--verbose", action="store_true", help="Zeigt Infos an")
    outputgroup.add_argument("-q", "--quit", action="store_true", help="Liefert nur den wahrscheinlichsten Key zurück")

    args = parser.parse_args()

    result: str

    if not os.path.exists(args.infile):
        sys.stderr.write(args.infile + ": " + os.strerror(2))
    else:
        with open(args.infile, "r") as f:
            text: str = f.read()

        if args.cipher in ["c", "caesar"]:

            caesar = Caesar()
            res = caesar.crack(text)

            if args.verbose:
                print(f"Cracking Caesar-encypted file {args.infile}: Key = {res[0]}")
            else:
                print(res[0])

        elif args.cipher in ["v", "vigenere"]:

            kasisiki = Kasiski(text)
            len = kasisiki.ggt_count([kasisiki.dist_n_list(text, i) for i in range(3, 10)][0]).most_common(1)[0][0]
            res = kasisiki.crack_key(len)

            if args.verbose:
                print(f"Cracking Caesar-encypted file {args.infile}: Key = {res}")
            else:
                print(res)
