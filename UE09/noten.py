__author__ = "Hanno Postl"
__version__ = "1.0"
__status__ = "Finished"

import pandas as pd
import argparse

noten = r'C:\Users\hanno\PycharmProjects\2324_4cn_0152_sew4_sem1p\UE09\res\noten.csv'
alleNoten = r'C:\Users\hanno\PycharmProjects\2324_4cn_0152_sew4_sem1p\UE09\res\result_all.csv'
sewNoten = r'C:\Users\hanno\PycharmProjects\2324_4cn_0152_sew4_sem1p\UE09\res\result_SEW.csv'

if __name__ == "__main__":
    # Argument parser for command line arguments
    parser = argparse.ArgumentParser(description="noten.py by Hanno Postl / HTL Rennweg")
    parser.add_argument("outfile", help="Ausgabedatei (z.B. result.csv)")
    parser.add_argument("-n", help="csv-Datei mit den Noten")
    parser.add_argument("-s", help="xml-Datei mit den Schülerdaten")
    parser.add_argument("-m", default="Nummer", help="Name der Spalte, die zu verknüpfen ist (default = Nummer)")
    parser.add_argument("-f", help="Name des zu filternden Gegenstandes (z.B. SEW)")

    # Group for output mode arguments
    outputgroup = parser.add_mutually_exclusive_group()
    outputgroup.add_argument("-v", "--verbose", action="store_true", help="Gibt die Daten Kommandozeile aus")
    outputgroup.add_argument("-q", "--quiet", action="store_true", help="keine Textausgabe")

    # Parse the arguments
    args = parser.parse_args()


    """allNotes = pd.read_csv(noten, header=0, sep=';')
    print(allNotes)"""