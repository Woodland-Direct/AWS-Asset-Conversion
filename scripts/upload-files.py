#!/usr/bin/env python3
"""Read, edit, and upload CSV file to AWS

Usage:
    python3 -i scripts/upload-files.py
"""

import boto3
import os
import requests
import re



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
            file_name = download_image(image, item_id, line[5])
            #upload_file_to_AWS(file_name, bucket)
            ns_name = line[5]
            ns_url = 'https://'+bucket+'/'+file_name
            ns_type = 9
            ns_mi = line[3]
            # upload_file_to_NS(ns_name,ns_url,ns_type,ns_mi)
        file.close()
    except Exception as e:
        print("Could not read file", e)

def download_image(download_url, item_id, file_identifier):
    """Download file locally from URL

    Args:
        download_url: String, url to image you want to download
        item_id: String, id of item for file name
        file_identifier: String, what image will be used for
    """
    try:
        url = download_url
        r = requests.get(url)
        d = r.headers['content-disposition']
        fname = re.findall("filename=(.+)", d)[0]
        identifier = strip_and_replace(file_identifier, ' ', '-')
        ext = get_file_ext(fname)
        file_path = "".join(["images/", item_id, '-', identifier, ext])
        with open(file_path, 'wb') as outfile:
            outfile.write(r.content)
        return file_path
    except Exception as e:
        print("Could not download file", e)

def strip_and_replace(str, text_to_replace, replace_with):	
    """	
    send a str and a replacement for it	
    """	
    return str.replace(text_to_replace, replace_with).strip("\n")


def get_file_ext(url):	
    """Gets the file extension from a url	
    Args:	
        url: url to image	
    """	
    return "." + url.split(".")[-1]

def upload_file_to_AWS(file_name, bucket):
    """Upload file to S3 Bucket

    Args:
        file_name: String, to path of file, this is also where you"ll name your file. "folder_name/file_name.jpg"
        bucket: String to AWS bucket
    """
    try:
        client.upload_file(file_name, bucket, file_name)
    except Exception as e:
        print("Could not upload file", e)


def upload_file_to_NS(ns_name, ns_url, ns_type, mi_id):
    """Upload the file to NS
    Args:
        file_name: the name we want on the asset record
        file_url: the url from AWS to reference the file
        ns_type: the id type of the asset (9 is default)
        ns_mi: the internalid of the mi in ns
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0',
                   'content-type': 'application/json'}
        data = {'assets': [{'custrecord_pa_title': ns_name,
                            'custrecord_pa_url': ns_url,
                            'custrecord_asset_type': ns_type,
                            'custrecord_pa_item': mi_id
                            }]}
        r = requests.post(
            'https://483668-sb1.extforms.netsuite.com/app/site/hosting/scriptlet.nl?script=1651&deploy=1&compid=483668_SB1&h=5cd761bfb4a02e9c71bf', json=data, headers=headers)
        print('status code: ', r.status_code)

    except Exception as e:
        print("Naw dog, should have done it better :|", e)
