"""
This script is used to merge data from a CSV file and an XML file based on a common column.
The CSV file contains grades, and the XML file contains student data.
The script supports both verbose and quiet modes.
The output is a CSV file that contains the merged data.

Author: Hanno Postl
Version: 1.4
Status: Finished
"""

import re
import pandas as pd
import argparse
import os
import sys


def read_xml(filename: str) -> pd.DataFrame:
    """
    This function reads an XML file and extracts specific data using regular expressions.
    The extracted data includes the student number, salutation, first name, last name, and date of birth.
    The data is then returned as a pandas DataFrame.

    :param filename: The name of the XML file to read.
    :return: A DataFrame containing the extracted data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(
        "<Schueler>\s*<Nummer>(.*?)</Nummer>\s*<Anrede>(.*?)</Anrede>\s*<Vorname>(.*?)</Vorname>\s*<Nachname>(.*?)</Nachname>\s*<Geburtsdatum>(.*?)</Geburtsdatum>",
        flags=re.DOTALL)
    result = re.findall(pattern, content)
    return pd.DataFrame(result, columns=['Nummer', 'Anrede', 'Vorname', 'Nachname', 'Geburtsdatum'], dtype=str)


if __name__ == "__main__":
    # Argument parser for command line arguments
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="noten.py by Hanno Postl / HTL Rennweg")
    parser.add_argument("outfile", help="Output file (e.g., result.csv)")
    parser.add_argument("-n", help="CSV file with grades")
    parser.add_argument("-s", help="XML file with student data")
    parser.add_argument("-m", default="Nummer", help="Name of the column to join on (default = Nummer)")
    parser.add_argument("-f", help="Name of the subject to filter (e.g., SEW)")

    # Group for output mode arguments
    outputgroup = parser.add_mutually_exclusive_group()
    outputgroup.add_argument("-v", "--verbose", action="store_true", help="Outputs the data to the command line")
    outputgroup.add_argument("-q", "--quiet", action="store_true", help="No text output")

    # Parse the arguments
    args = parser.parse_args()

    # Check if input files exist
    if not os.path.exists(args.n):
        sys.stderr.write(args.n + ": " + os.strerror(2))
    elif not os.path.exists(args.s):
        sys.stderr.write(args.s + ": " + os.strerror(2))
    else:
        # Read the CSV and XML files into DataFrames
        noten: pd.DataFrame = pd.read_csv(args.n, sep=';', dtype=str, encoding='utf-8')
        schueler: pd.DataFrame = read_xml(args.s)

        # Merge the DataFrames based on the specified column
        if args.f:
            result: pd.DataFrame = pd.merge(schueler, noten[["Nummer", args.f]], on='Nummer')
        else:
            result: pd.DataFrame = pd.merge(schueler, noten, on='Nummer')

        # Write the result to the output file
        result.to_csv(args.outfile, sep=';', index=False)

        # Print the result if verbose mode is on
        if args.verbose:
            print(f"""CSV file with grades : {args.n}
            XML file with student data : {args.s}
            Name of the column to join on : {args.m}
            Output file: {args.outfile}""")
        elif args.quiet:
            pass
        else:
            print(f"Output file: {args.outfile}")