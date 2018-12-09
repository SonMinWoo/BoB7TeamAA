import json
import os
from random import *

PATH = 'C:\\Users\\SonMinWoo\\Desktop\\maljson'

filenames = os.listdir(PATH)

fcount = 0
leakcount = 0
"""
for file in range(len(filenames)):
    fcount = fcount+1
    if (fcount > 99):
        break
    try:
        with open(PATH + "/" + file) as f:
            data = json.load(f)
        if(len(data['dataleaks']) > 1):
            print(data['apkName'])
            leakcount = leakcount+1
    except:
        pass
"""

for r in range(100):
        r = randint(0, len(filenames))
        fcount = fcount+1
        if (fcount > 99):
            break
        try:
            with open(PATH + "/" + filenames[r]) as f:
                data = json.load(f)
            if(len(data['dataleaks']) > 1):
                print(data['apkName'])
                leakcount = leakcount+1
        except:
            pass

print(leakcount)
