import os
import json
import time

base = 'D:/Linkedin/'

# Open and read the folders JSON file
with open('folders.json', 'r') as file:
    folders = json.load(file)

for d in os.walk(base):
    # print(f'Current Folder: {d[0]}, Subfolders: {d[1]}, Files: {d[2]}')
    if d[0] not in folders:
        print(f'Tracking folder {d[0]} now.')
        folders[d[0]] = {}

    for file in d[2]:
        if file not in folders[d[0]]:
            print(f'Tracking file {file} now.')
            folders[d[0]][file]=os.path.getmtime(d[0]+'/'+file)

            # to-do
            # upload_to_s3(file)


with open('folders.json','w') as file:
    file.write(json.dumps(folders))