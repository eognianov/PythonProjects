city = input().lower()
s = float(input())
com = -1.0
if city == 'sofia':
    if 0 <= s <= 500:
        com = s * 5/100
    elif 500 < s <= 1000:
        com = s * 7/100
    elif 1000 < s <= 10000:
        com = s * 8/100
    elif s > 10000:
        com = s * 12/100
elif city == 'varn':
    if 0 <= s <= 500:
        com = s * 4.5/100
    elif 500 < s <= 1000:
        com = s * 7.5/100
    elif 1000 < s <= 10000:
        com = s * 10/100
    elif s > 10000:
        com = s * 13/100
elif city == 'plovdiv':
    if 0 <= s <= 500:
        com = s * 5.5/100
    elif 500 < s <= 1000:
        com = s * 8/100
    elif 1000 < s <= 10000:
        com = s * 12/100
    elif s > 10000:
        com = s * 14.5/100
if com !=-1.0:
    print('{0:.2f}'.format(com))
else:
    print('error')