import re
text = input()
patternForSpaces = r'\+359 2 \d{3} \d{4}\b'
patternForDashes = r'\+359-2-\d{3}-\d{4}\b'
matchOne=re.search(patternForDashes,text)
matchTwo=re.search(patternForSpaces,text)

print(matchOne)
print(matchTwo)

