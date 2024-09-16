import os
import json
import time

def upload_to_s3(file):
    # complete implementation
    return True

def backup():
    base = 'D:/Linkedin/'

    # Open and read the folders JSON file
    with open('folders.json', 'r') as file:
        folders = json.load(file)

    for d in os.walk(base):
        # print(f'Current Folder: {d[0]}, Subfolders: {d[1]}, Files: {d[2]}')
        folder = d[0].replace('\\','/')
        if d[0] not in folders:
            print(f'Tracking folder {folder} now.')
            folders[folder] = {}

        for file in d[2]:
            if file not in folders[folder]:
                print(f'Tracking file {folder + file} now.')
                folders[folder][file]=os.path.getmtime(folder+'/'+file)

                upload_to_s3(file)

            if folders[folder][file] < os.path.getmtime(folder+'/'+file):
                print(f'Backed up file {file} to latest version.')


    with open('folders.json','w') as file:
        file.write(json.dumps(folders))

    return True

backup()