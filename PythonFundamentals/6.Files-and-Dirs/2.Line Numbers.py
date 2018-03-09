inputFile=open('Input1.txt')
outputFile=open('Output1.txt','w')
allInputlines = inputFile.readlines()
numberOfLines=len(allInputlines)
for i in range(0,numberOfLines):
    currentline =allInputlines[i]
    outputFile.write(str(i+1)+'. ' + currentline)
inputFile.close()
outputFile.close()