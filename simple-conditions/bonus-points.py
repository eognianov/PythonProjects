num=int(input())
bonus = 0
if num <= 100:
    bonus +=5
elif num > 1000:
    bonus += 10 * num / 100
elif num > 100 :
    bonus += 20 * num / 100
if num % 2 == 0:
    bonus += 1
if num % 10 == 5 :
    bonus += 2
print(bonus)
print(num+bonus)