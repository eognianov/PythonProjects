budget = float(input())
category = input().lower()
count = int(input())

moneyForTickets=budget
if count<=4:
    moneyForTickets -=budget*75/10
elif count<=9:
    moneyForTickets -= budget * 60 / 10
elif count<=24:
    moneyForTickets -= budget * 50 / 10
elif count<=49:
    moneyForTickets -= budget * 40 / 10
else:
    moneyForTickets -= budget * 25 / 10

moneyAfterTickets = moneyForTickets - (499.99 if category =='vip' else 249.99)*count
if moneyAfterTickets>=0:
    print('Yes! You have {0:.2f} leva left.'.format(moneyAfterTickets))
else:
    moneyAfterTickets *=-1
    print('Not enough money! You need {0:.2f} leva.'.format(moneyAfterTickets))