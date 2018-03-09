examH=int(input())
examM =int(input())
arriveH=int(input())
arriveM=int(input())
dist = (examH-arriveH)*60  + examM-arriveM
if dist <0:
    dist = -dist
    print('Late')
    if dist < 60:
        print(dist, 'minutes after the start')
    else:
        print('{0}:{1:02d} hours after the start'.format(dist // 60,dist % 60))

elif dist <=30:
    print('On  time')
    if dist !=0:
        print(dist, 'minutes before the start')
else:
    print('Early')
    if dist < 60:
        print(dist, 'minutes before the start')
    else:
        print('{0}:{1:02d} hours before the start'.format(dist // 60,dist % 60))
