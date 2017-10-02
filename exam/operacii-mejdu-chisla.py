n1=int(input())
n2=int(input())
operator=input()
try:
    if operator=='+':
        res = n1+n2
        print('{0} + {1} = {2} -'.format(n1,n2,res),end=' ')
        if res % 2 ==0:
            print('even')
        else:
            print('odd')
    elif operator=='-':
        res = n1 - n2
        print('{0} - {1} = {2} -'.format(n1, n2, res), end=' ')
        if res % 2 == 0:
            print('even')
        else:
            print('odd')
    elif operator=='*':
        res = n1 * n2
        print('{0} * {1} = {2} -'.format(n1, n2, res), end=' ')
        if res % 2 == 0:
            print('even')
        else:
            print('odd')
    elif operator=='/':
        res = n1 / n2
        print('{0} / {1} = {2:.2f}'.format(n1, n2, res))
    elif operator=='%':
        res = n1 % n2
        print('{0} % {1} = {2}'.format(n1, n2, res))
except ZeroDivisionError:
    print('Cannot divide {0} by zero'.format(n1))