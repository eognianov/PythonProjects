import math
x=int(input())
y=float(input())
z=int(input())
br=int(input())

if (float(z)>x*4*y/25):
    print('It will be a tough winter! More {0:.0f} liters wine needed.'.format(math.floor(float(z)-x*4*y/25)))
else:
    print('Good harvest this year! Total wine: {0:.0f} liters.'.format(math.floor(x*4*y/25)))
    print('{0:.0f} liters left -> {1:.0f} liters per person.'.format(math.ceil(x*4*y/25-z),math.ceil((x*4*y/25-z)/br)))