"""
Author: Hanno Postl
Version: 1.2
Status: Finished
"""


import os
from collections.abc import Iterable, Generator
from typing import TextIO

def get_all_files(pathname: os.PathLike | str):
    """Yield all files in pathname and all its subdirectories."""
    for name in os.listdir(pathname):
        full_path = os.path.join(pathname, name)
        if os.path.isdir(full_path):
            yield from get_all_files(full_path)
        else:
            yield full_path

def open_files(filenames: Iterable[str]) -> Generator[TextIO, None, None]:
    """
    Generator function to open files and yield file handles.

    :param filenames: Iterable of filenames
    :return: Generator yielding file handles
    """
    for fn in filenames:
        with open(fn) as f:
            yield f


def read_lines(files: Iterable[TextIO]) -> Generator[str, None, None]:
    """
    Generator function to read lines from file handles.

    :param files: Iterable of file handles
    :return: Generator yielding lines
    """
    for f in files:
        for line in f:
            yield line.rstrip()


def print_lines(lines: Iterable[str]) -> None:
    """
    Function to print lines, stripping trailing whitespace.

    :param lines: Iterable of lines
    """
    for line in lines:
        print(line)

if __name__ == "__main__":
    # Alle Dateien im aktuellen Verzeichnis und allen Unterverzeichnissen ausgeben
    for file in get_all_files(r"C:\Users\hanno\PycharmProjects\2324_4cn_0152_sew4_sem1p\UE10"):
        print(file)

    fl = get_all_files(".")  # fl = "Liste" mit Filenamen
    of = open_files(fl)  # of = "Liste" mit offenen Files
    lines = read_lines(of)
    print_lines(lines)