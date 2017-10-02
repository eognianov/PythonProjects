import math
year =input().lower()
p = int(input())
h = int(input())
weekends = 48 - h
games = 0
games = 2/3 * p
games += weekends * 3/4
games += h
if year == 'leap':
    games += 15 * games / 100
games = math.floor(games)
print (games)