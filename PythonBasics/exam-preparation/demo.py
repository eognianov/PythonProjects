phonebook = dict()
text = input().split(' ')
phonebook['Ivanov'] = {'mobielen': '12131321213',
                       'domashen': 'nqma'}
phonebook[text[0]] = {text[1]:text[2]}
print(phonebook)
for lichno in phonebook.keys():
    for tip in phonebook[lichno]:
        print('{} - {} - {}'.format(lichno, tip, phonebook[lichno][tip]))
#phonebook.pop('Ivanov')
print('\n')
for lichno in phonebook.keys():
    for tip in phonebook[lichno]:
        print('{} - {} - {}'.format(lichno, tip, phonebook[lichno][tip]))
print('\n')

phonebook['Ivanov'].pop('mobielen')
for lichno in phonebook.keys():
    for tip in phonebook[lichno]:
        print('{} - {} - {}'.format(lichno, tip, phonebook[lichno][tip]))