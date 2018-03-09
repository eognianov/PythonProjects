age = float(input())
pol = input().lower()

if age >= 16:
    if pol == 'm':
        print('Mr.')
    elif pol == 'f':
        print('Ms.')
else:
    if pol == 'm':
        print('Master')
    elif pol == 'f':
        print('Miss')