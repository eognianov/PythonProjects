def check_number(num):
    re = 0
    if num > 0:
        re=1
    elif num < 0:
        re=2
    return re
number = int(input())
if check_number(number)==0:
    print('The number {0} is zero.'.format(number))
elif check_number(number)==1:
    print('The number {0} is positive.'.format(number))
elif check_number(number)==2:
    print('The number {0} is negative.'.format(number))