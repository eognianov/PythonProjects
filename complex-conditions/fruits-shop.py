fruit = input().lower()
day = input().lower()
q = float(input())
price = -1.0
if day == 'sunday' or day == 'saturday':
    if fruit == 'banana':
        price = q * 2.70
    elif fruit == 'apple':
        price = q * 1.25
    elif fruit == 'orange':
        price == q * 0.90
    elif fruit == 'grapefruit':
        price == q *1.60
    elif fruit == 'kiwi':
        price = q * 3
    elif fruit == 'pineapple':
        price = q * 5.6
    elif fruit == 'grapes':
        price = q * 4.20

elif day == 'monday' or day == 'tuesday' or day ==  'wednesday' or day == 'thursday' or day == 'friday':
    if fruit == 'banana':
        price = q * 2.50
    elif fruit == 'apple':
        price = q * 1.20
    elif fruit == 'orange':
        price == q * 0.85
    elif fruit == 'grapefruit':
        price == q * 1.45
    elif fruit == 'kiwi':
        price = q * 2.70
    elif fruit == 'pineapple':
        price = q * 5.5
    elif fruit == 'grapes':
        price = q * 3.85

if price !=-1.0:
     print('{0:.2f}'.format(price))
else:
    print('error')
