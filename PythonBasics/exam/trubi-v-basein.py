v=int(input())
p1=int(input())
p2=int(input())
h=float(input())
h*=100
h=int(h)
v*=100
v1 = p1*h
v2=p2*h

if (v1+v2<v):
    P1=v1*100//(v1+v2)
    P2=v2*100//(v1+v2)
    full=(v1+v2)*100//v
    # if (P1==P1//1):
    #     pipe1=int(P1)
    # else:
    #     pipe1='{0:.2f}'.format(P1)
    # if (P2==P2//1):
    #     pipe2=int(P2)
    # else:
    #     pipe2='{0:.2f}'.format(P2)
    print('The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%.'.format(full,P1,P2))
else:
    print('For {0} hours the pool overflows with {1} liters.'.format(h/100,(-v+v1+v2)/100))