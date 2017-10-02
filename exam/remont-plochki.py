N = float(input())
W = float(input())
L = float(input())
M = float(input())
O = float(input())

area = N * N
areaTile = W * L
areaBench = M * O
areaForTiles = area - areaBench
contTiles = areaForTiles / areaTile
time = contTiles * 0.2
print('{0:.2f}'.format(contTiles))
print('{0:.2f}'.format(time))
