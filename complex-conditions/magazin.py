prod = input().lower()
city = input().lower()
qu = float(input())
price = 1
if city == 'sofia':
    if prod == 'coffee':
        price = qu * 0.5
    elif prod == 'water':
        price = qu * 0.8
    elif prod == 'beer':
        price = qu * 1.2
    elif prod == 'sweets':
        price = qu * 1.45
    elif prod == 'peanuts':
        price = qu * 1.6
elif city == 'plovdiv':
    if prod == 'coffee':
        price = qu * 0.4
    elif prod == 'water':
        price = qu * 0.7
    elif prod == 'beer':
        price = qu * 1.15
    elif prod == 'sweets':
        price = qu * 1.30
    elif prod == 'peanuts':
        price = qu * 1.5
elif city == 'varna':
    if prod == 'coffee':
        price = qu * 0.45
    elif prod == 'water':
        price = qu * 0.7
    elif prod == 'beer':
        price = qu * 1.1
    elif prod == 'sweets':
        price = qu * 1.35
    elif prod == 'peanuts':
        price = qu * 1.55
print('{0:.2f}'.format(price))