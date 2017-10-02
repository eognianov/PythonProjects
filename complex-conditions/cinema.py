type = input().upper()
r = int(input())
c = int(input())

cnt = r * c
price = -1

if type == 'PREMIERE':
    price = cnt * 12
elif type == 'NORMAL':
    price = cnt * 7.5
elif type == 'DISCOUNT':
    price = cnt * 5

print('{0:.2f} leva'.format(price))