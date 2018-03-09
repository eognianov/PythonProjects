import  re

pattern = r'<a href=\"(.+?)\">(.+?)</a>'
regex = re.compile(pattern)
inputline = input()
allText = ''
while inputline != 'end':
    allText += inputline
    inputline=input()
lastIndex = 0
match = regex.search(allText, lastIndex)
replacedString=allText
while match != None:
    oldString = match.group(0)
    url = match.group(1)
    anchorText = match.group(2)
    lastIndex=match.end()
    newString = '[URL href={0}]{1}[/URL]'.format(url,anchorText)
    replacedString=replacedString.replace(oldString,newString)
    match = regex.search(allText, lastIndex)
print(replacedString)