import math
n = int(input())
is_prime = True
if n < 2:
    print('Not Prime')
else:
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            print('Not Prime')
            is_prime = False
            break
    if is_prime:
        print('Prime')