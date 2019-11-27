#!/usr/bin/env python3
"""Read, edit, and upload CSV file to AWS

Usage: 

    python3 upload-files.py <URL>
"""

def read_file(file_path):
    """Opens files and prints every line.

    Args:
        file_path: CSV file name in the root directory of folder.

    Returns:
        A list of strings containing all rows, with columns seperated by a comma.
    """
    try:
        file = open(file_path, "r")
        for item in file:
            upload_file(item.split(","))
        file.close()
    except Exception as e:
        print("Could not read file", e)

def edit_file(file_path, add):
    """Adds a new line to your file

    Args:
        file_path: CSV file name in the root directory of folder.
        add: string to be written on the file, with columns seperated by commas
    """
    try:
        file = open(file_path, "a")
        file.write("\n" + add)
        file.close()
    except Exception as e:
        print("Could not edit file", e)


def upload_file(item):
    print(item[0])
    print(item[1].strip('\n'))
