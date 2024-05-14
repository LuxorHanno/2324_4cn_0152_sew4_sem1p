__author__ = "Hanno Postl"
__version__ = "1.0"
__status__ = "Finished"

import pandas as pd
import argparse

r"""noten = r'C:\Users\hanno\PycharmProjects\2324_4cn_0152_sew4_sem1p\UE09\res\noten.csv'
schueler = r'C:\Users\hanno\PycharmProjects\2324_4cn_0152_sew4_sem1p\UE09\res\schueler.xml'
"""

import re
import pandas as pd
import argparse
import os
import sys


def read_xml(filename: str) -> pd.DataFrame:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile("<Schueler>\s*<Nummer>(.*?)</Nummer>\s*<Anrede>(.*?)</Anrede>\s*<Vorname>(.*?)</Vorname>\s*<Nachname>(.*?)</Nachname>\s*<Geburtsdatum>(.*?)</Geburtsdatum>", flags=re.DOTALL)
    result = re.findall(pattern, content)
    df = pd.DataFrame(result, columns=['Nummer', 'Anrede', 'Vorname', 'Nachname', 'Geburtsdatum'], dtype=str)
    return df

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

    # Check if input file exists
    if not os.path.exists(args.n):
        sys.stderr.write(args.n + ": " + os.strerror(2))
    elif not os.path.exists(args.s):
        sys.stderr.write(args.s + ": " + os.strerror(2))
    else:
        # Read the input files
        noten = pd.read_csv(args.n, sep=';', dtype=str, encoding='utf-8')
        schueler = read_xml(args.s)


        # Merge the dataframes
        result = pd.merge(schueler, noten, on='Nummer')
        print (result)

        # Filter the data
        if args.f:
            result = result[result['Gegenstand'] == args.f]

        # Write the result to a csv file
        result.to_csv(args.outfile, sep=';',index=False)

        # If verbose mode is on
        if args.verbose:
            print(f"""csv-Datei mit den Noten : {args.n}
            xml-Datei mit den Schülerdaten : {args.s}
            Name der Spalte, die zu verknüpfen ist : {args.m}
            Output-Datei: {args.outfile}""")
        elif args.quiet:
            pass
        else:
            print(f"Output-Datei: {args.outfile}")