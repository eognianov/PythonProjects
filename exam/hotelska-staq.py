month = input().lower()
count = int(input())
studioPrice = -1
apartamentPrice = -1
if month == 'may' or month== 'october':
    studioPrice = 50
    apartamentPrice = 65
    if count >14:
        studioPrice -= studioPrice*30/100
    elif count>7:
        studioPrice-=studioPrice*5/100
elif month == 'june' or month == 'septembre':
    studioPrice = 75.20
    apartamentPrice=68.70
    if count > 14:
        studioPrice-=studioPrice*20/100
else:
    studioPrice = 76
    apartamentPrice = 77
if count>14:
    apartamentPrice-=apartamentPrice*10/100

print('Apartment: {0:.2f} lv.\nStudio: {1:.2f} lv.'.format(apartamentPrice*count,studioPrice*count))