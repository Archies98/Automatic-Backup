import os
import json
import time
import boto3
from botocore.config import Config

def upload_to_s3(file):
    # complete implementation
    with open('configuration.json','r') as config:
        credentials = config['s3_credentials']

    s3 = boto3.client(
        service = 's3',
        region_name = 'us-east-1',
        aws_access_key_id = credential['AWS_ACCESS_KEY'],
        aws_secret_access_key = credential['AWS_SECRET_ACCESS_KEY']
    )

    s3.Bucket('backup-app-storage').upload_file(file, file)

    return True

def backup():
    base = 'D:/Linkedin/'

    # Open and read the folders JSON file
    with open('folders.json', 'r') as file:
        folders = json.load(file)

    for d in os.walk(base):
        # print(f'Current Folder: {d[0]}, Subfolders: {d[1]}, Files: {d[2]}')
        folder = d[0].replace('\\','/')
        if folder not in folders:
            print(f'Tracking folder {folder} now.')
            folders[folder] = {}

        for file in d[2]:
            if file not in folders[folder]:
                print(f'Tracking file {folder + '/' + file} now.')
                folders[folder][file]=os.path.getmtime(folder+'/'+file)

                upload_to_s3(folder+'/'+file)

            if folders[folder][file] < os.path.getmtime(folder+'/'+file):
                print(f'Backed up file {file} to latest version.')


    with open('folders.json','w') as file:
        file.write(json.dumps(folders))

    return True

backup()