n = int(input())
leftRight = (n-1)//2
for i in range (((n-1//2)+1)):
    print('-' * leftRight, end = '')
    print('*', end='')
    mid=n-(2*leftRight)-2
    if mid >= 0:
        print('-'*mid, end='')
        print('*', end='')
    print('-'*leftRight)
    leftRight-=1
