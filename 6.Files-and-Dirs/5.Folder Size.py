import os
allBytes=0
for dirPath, dirnames, filenames in os.walk('./Folder Size/TestFolder'):
    if dirnames == []:
        for fileName in filenames:
            allBytes+=os.stat(os.path.join(dirPath,fileName)).st_size
            #print(os.stat(os.path.join(dirPath,fileName)).st_size)
            #print(os.stat(dirPath+'/'+fileName).st_size)
print(allBytes/(1024*1024))