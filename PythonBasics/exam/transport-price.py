n = int(input())
dn = input().lower()
min_cost=0
if dn =='day':
    min_cost= 70+79*n
else:
    min_cost=70+90*n
if n >= 20:
    min_cost= min(min_cost,n*9)
if n>=100:
    min_cost=min(min_cost,n*6)
print(min_cost/100)