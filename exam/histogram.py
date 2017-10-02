n = int(input())
p1,p2,p3,p4,p5 = 0,0,0,0,0
for i in range(n):
    a = int(input())
    if (a<200):
        p1+=1
    elif (a<=399):
        p2+=1
    elif (a<=599):
        p3+=1
    elif (a<=799):
        p4+=1
    else:
        p5+=1
p1 = p1*100/n
p2 = p2*100/n
p3 = p3*100/n
p4 = p4*100/n
p5 = p5*100/n

print('{:.2f}%\n{:.2f}%\n{:.2f}%\n{:.2f}%\n{:.2f}%'.format(p1,p2,p3,p4,p5))