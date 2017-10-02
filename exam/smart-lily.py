y = int(input())
peralniq = float(input())
p = int(input())
n = y//2
money = n*(1+n)//2*10 - n + (y-n)*p
if peralniq > money:
    print('No! {0:.2f}'.format(peralniq-money))
else:
    print('Yes! {0:.2f}'.format(money-peralniq))