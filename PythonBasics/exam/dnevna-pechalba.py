workDays = int(input())
moneyPerDay = float(input())
USDrate = float(input())

moneyPerMonth = workDays * moneyPerDay
moneyPerYear = moneyPerMonth*145/10
earnPerYear = moneyPerYear - moneyPerYear*25/100
earnPerYearLV = earnPerYear*USDrate
earnPerYearLV /= 365
print('{0:.2f}'.format(earnPerYearLV))

