import math

lenght = int(input())
width = float(input())

lenght*=100

if math.floor(width) == math.ceil(width): #proverqvame dali chisloto e cqlo
    try:
        if lenght % int(width)==0:
            print('{0:.2f}'.format(lenght*width))
            #print('%.2f'%(lenght*width))
        else:
            print('{0:.2f}%'.format(lenght/width*100))
    except(ZeroDivisionError):
        print('{0:.2f}'.format(lenght * width))
else:
    print('{0:.2f}'.format(lenght * width))


