state = input()
while state != 'collapse':
    fiction=input()
    while fiction != '':
        state = state.replace(fiction,'')
        fiction = fiction[1:len(fiction)-1]
    if state == '':
        print('(void)')
    else:
        print(state.strip())
    state=input()
