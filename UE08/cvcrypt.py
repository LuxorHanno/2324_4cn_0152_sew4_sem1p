__author__ = "Hanno Postl"
__version__ = "1.1"
__status__ = "work in progress"


import argparse
from Caesar import Caesar
from Vigenere import Vigenere


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using Caesar cipher.")
    parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt"], help="Mode of operation: encrypt or decrypt")
    parser.add_argument("-t", "--text", help="Text to be processed")
    parser.add_argument("-k", "--key", help="Key to be used for encryption or decryption")

    args = parser.parse_args()

    caesar = Caesar()

    if args.mode == "encrypt":
        if args.key:
            result = caesar.encrypt(args.text, args.key)
        else:
            result = caesar.encrypt(args.text)
    elif args.mode == "decrypt":
        if args.key:
            result = caesar.decrypt(args.text, args.key)
        else:
            result = caesar.decrypt(args.text)

    print(result)


