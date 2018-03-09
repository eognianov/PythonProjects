n = int(input())
p1,p2,p3 = 0,0,0
for i in range(n):
    a = int(input())
    if (a%2==0):
        p1+=1
    if (a%3==0):
        p2+=1
    if (a%4==0):
        p3+=1
p1 = p1*100/n
p2 = p2*100/n
p3 = p3*100/n


print('{:.2f}%\n{:.2f}%\n{:.2f}%'.format(p1,p2,p3))