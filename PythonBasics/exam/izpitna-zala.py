h = float(input())
w = float(input())
h *= 100
w *= 100
w-=100
placeR = w // 70
placeD = h // 120
allPlaces = int(placeD * placeR)
allPlaces -=3
print(allPlaces)