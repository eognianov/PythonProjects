pV = float(input())
pF = float(input())
mV = int(input())
mF = int(input())

price = mV * pV + mF * pF
price/=1.94
print(price)