n=int(input())
if (n==1):
    print('*')
if (n==2):
    print('**')
else:
    if (n%2==0):
        pos1, pos2 = n//2,n//2+1
    else:
        pos1,pos2=(n+1)//2,(n+1)//2
    total_row = n-(1-n%2)
    for row in range(total_row//2):
        for col in range(1,n+1):
            if(col == pos1 or col == pos2):
                print('*',end='')
            else:
                print('-',end='')
        print()
        pos1-=1
        pos2+=1
    for row in range(total_row-total_row//2):
        for col in range(1,n+1):
            if(col == pos1 or col == pos2):
                print('*',end='')
            else:
                print('-',end='')
        print()
        pos1+=1
        pos2-=1
