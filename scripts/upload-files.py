#!/usr/bin/env python3
"""Read, edit, and upload CSV file to AWS

Usage: 

    python3 upload-files.py <URL>
"""

def read_file(file_path):
    try:
        file = open(file_path, "r")
        for item in file:
            print(item)
        file.close()
    except Exception as e:
        print("Could not read file", e)

# def edit_file():
#     try:
#         file = open("students.txt", "a")
#         file.write("filler")
#         file.close()
#     except Exception:
#         print("Could not edit file")


# def upload_file():
#     print('upload')
