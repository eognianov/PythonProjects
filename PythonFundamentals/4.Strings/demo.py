text = 'Hello Betty! How are you Betty?. Is life good Betty?'
censordText=text.replace('Betty','*'*len('Betty'))
print(censordText)