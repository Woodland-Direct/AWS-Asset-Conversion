#!/usr/bin/env python3
"""Read, edit, and upload CSV file to AWS

Usage: 

    python3 upload-files.py <URL>
"""

import boto3
import urllib

client = boto3.client('s3', region_name='us-west-2')

def read_file(file_path, bucket):
    """Opens files and prints every line.

    Args:
        file_path: CSV file name in the root directory of folder.
        bucket: String to AWS bucket

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


def upload_file(item, bucket):
    """Upload file to S3 Bucket

    Args:
        item: Array containing img url and item name
        bucket: String to AWS bucket
    """
    try:
        fileName = 'images/' + item[0]
        image = item[1].strip('\n')
        imgPath = fileName + '.jpg'
        urllib.request.urlretrieve(image, imgPath)
        client.upload_file(imgPath, bucket, fileName)
    except Exception as e:
        print("Could not upload file", e)
