import os
import time
import shutil
import json

if(os.path.exists('./settings.json') == False):
   with open('./settings.json', 'w') as settings:
        settings.write('{"folderLocation":"./"}')

if(os.path.exists('./locations.json') == False):
    with open('./locations.json', 'w') as locations:
        locations.write('[]')

with open('./settings.json', 'r') as settings:
    folderLocation = json.loads(settings.read())['folderLocation']

while (True):
    with open('./locations.json', 'r') as locations:
        locations = json.loads(locations.read())
    files = os.listdir(folderLocation)
    for fileName in files:
    
        if(fileName != "Python Organizer.exe" and fileName != "settings.json" and fileName != "locations.json"):
            extension = fileName.split('.')[-1::][0]

            for location in locations:
                try:
                    isLocation = location['extensions'].index(extension) > -1
            
                    actualFileLocation = os.path.join(folderLocation, fileName)
                    destFileLocation = os.path.join(location['to'], fileName)
                    if(os.path.exists(location['to']) == False):
                        os.mkdir(location['to'])
                    os.rename(actualFileLocation, destFileLocation)
                    shutil.move(actualFileLocation, destFileLocation)
                    os.replace(actualFileLocation, destFileLocation)
                    print(f'Se encontro un archivo {destFileLocation}')
                except:
                    pass
                
    time.sleep(1)
    

