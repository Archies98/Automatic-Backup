import os

base = 'D:/Linkedin/'

for d in os.walk(base):
    print(d)