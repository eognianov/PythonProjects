n = int(input())
L = int(input())

for _1 in range(1, n+1):
    for _2 in range(1,n+1):
        for _3 in range(L):
            for _4 in range(L):
                for _5 in range(max(_1,_2)+1,n+1):
                    print(str(_1)+str(_2)+str(chr(ord('a')+_3))+str(chr(ord('a')+_4))+str(_5), end=' ')
print()