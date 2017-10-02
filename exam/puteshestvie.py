budget = float(input())
season = input().lower()

if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        print('Camp - {0:.2f}'.format(budget*30/100))
    else:
        print('Hotel - {0:.2f}'.format(budget*70/100))
elif budget<=1000:
    print('Somewhere in Balkans')
    if season == 'summer':
        print('Camp - {0:.2f}'.format(budget*40/100))
    else:
        print('Hotel - {0:.2f}'.format(budget*80/100))
else:
    print('Somewhere in Europe')
    print('Hotel - {0:.2f}'.format(budget*90/100))