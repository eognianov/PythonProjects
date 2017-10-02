import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def read_point():
    inputLine=input()
    inputDate=inputLine.split(' ')
    x=int(inputDate[0])
    y=int(inputDate[1])
    myPoint =  Point(x,y)
    return myPoint

def distance_between_points(pointOne, pointTwo):
    deltaX = pointOne.x - pointTwo.x
    deltaY = pointOne.y - pointTwo.y
    distance = math.sqrt(deltaX*deltaX+deltaY*deltaY)
    return distance

pointOne = read_point()
pointTwo = read_point()
distance=distance_between_points(pointOne,pointTwo)
print('{0:.3f}'.format(distance))