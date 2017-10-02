friend1 = input().lower()
friend2 = input().lower()

if (friend1 == 'out') ^ (friend2 == 'out'):
    print('Go out!')
else:
    print('Stay at home!')