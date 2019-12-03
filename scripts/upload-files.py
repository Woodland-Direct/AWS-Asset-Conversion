#!/usr/bin/env python3
"""Read, edit, and upload CSV file to AWS

Usage: 

    python3 upload-files.py <URL>
"""

import boto3
import urllib
import os

client = boto3.client("s3", region_name="us-west-2")

def read_file(file_path, bucket):
    """Opens files and prints every line.

    Args:
        file_path: CSV file name in the root directory of folder.
        bucket: String to AWS bucket
    """
    try:
        if not os.path.exists("images/"):
            os.makedirs("images/")

        file = open(file_path, "r")
        for item in file:
            line = item.split(",")
            image = line[1].strip("\n")
            item_id = line[0]
            file_ext = get_file_ext(image)
            file_name = "".join(["images/", item_id, file_ext])
            download_image(image, file_name)
            upload_file(file_name, bucket)
        file.close()
    except Exception as e:
        print("Could not read file", e)

def get_file_ext(url):
    """Gets the file extension from a url

    Args:
        url: url to image
    """
    return "." + url.split(".")[-1]


def download_image(download_url, save_file_path):
    """Download file locally from URL

    Args:
        download_url: String, url to image you want to download
        save_file_path: String, to path of file, this is also where you"ll name your file. "folder_name/file_name.jpg
    """
    try:
        urllib.request.urlretrieve(download_url, save_file_path)
    except Exception as e:
        print("Could not download file", e)


def upload_file(file_name, bucket):
    """Upload file to S3 Bucket

    Args:
        file_name: String, to path of file, this is also where you"ll name your file. "folder_name/file_name.jpg
        bucket: String to AWS bucket
    """
    try:
        client.upload_file(file_name, bucket, file_name)
    except Exception as e:
        print("Could not upload file", e)
