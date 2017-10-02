import os
filestat=os.stat('Input1.txt')
print(filestat.st_size)