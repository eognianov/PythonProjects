h = int(input())
x = int(input())
y = int(input())

if (0 < x < 3*h and 0 < y < h) or (h <= x < 2 * h and 4 * h > y > 0):
    print('inside')
elif (y == 0 and 0 <= x <= 3*h) or ((x == 0 or x == 3*h) and 0 <= y <= h) or ((y == h) and (0 <= x <= h or 2*h <= x <= 3*h)) or ((y==4*h) and h <= x <=2*h) or ((x== h or x==2*h) and h <= y <= 4*h):
    print('border')
else:
    print('outside')

