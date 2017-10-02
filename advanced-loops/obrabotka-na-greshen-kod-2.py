n = 0
while True:
    print('Enter even number: ', end='')
    try:
        n=int(input())
    except:
        print('Invalid numer!')
        continue
    if n % 2 == 0:
        break
    print('This number is not even.')
print('Even number entered:', n)