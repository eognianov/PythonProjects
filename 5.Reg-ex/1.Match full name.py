import re
pattern = r'\b([A-Z][a-z]+) ([A-Z][a-z]+)\b'
text = input()
match = re.search(pattern,text)
if match != None:
    print(match.group(0))