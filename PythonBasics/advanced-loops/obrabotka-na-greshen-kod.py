n = 0
while True:
    n = int(input('Enter even numer: '))
    if n % 2 == 0:
        break
    print('This number is not even.')
print('Even number entered:', n)
