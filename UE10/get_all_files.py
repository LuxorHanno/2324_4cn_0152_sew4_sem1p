"""
Author: Hanno Postl
Version: 1.2
Status: Finished
"""


import os
def get_all_files(pathname):
    """Yield all files in pathname and all its subdirectories."""
    for name in os.listdir(pathname):
        full_path = os.path.join(pathname, name)
        if os.path.isdir(full_path):
            yield from get_all_files(full_path)
        else:
            yield full_path

if __name__ == "__main__":
# Alle Dateien im aktuellen Verzeichnis und allen Unterverzeichnissen ausgeben
    for file in get_all_files(r"C:\Users\hanno\PycharmProjects\2324_4cn_0152_sew4_sem1p\UE10"):
        print(file)