n = int(input())
stars = 1
if n % 2 == 0:
    stars+=1
for i in range((n+1)//2):
    padding=(n-stars)//2
    print('-' * padding, end='')
    print('*' * stars, end='')
    print('-' * padding)
    stars +=2
for i in range(n//2):
    print('|'+'*'*(n-2)+'|')