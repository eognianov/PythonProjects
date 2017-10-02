censoredWordsString=input()
text = input()
censoredWords=censoredWordsString.split(', ')
for word in censoredWords:
    text = text.replace(word, '*' * len(word))
print(text)