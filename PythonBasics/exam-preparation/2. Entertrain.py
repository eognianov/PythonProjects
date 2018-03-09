pow = int(input())
curr = input()
wagons = []
currPow = 0
while curr != 'All ofboard!':
    wagons += [int(curr)]
    currPow += wagons[-1]
    if currPow > pow:
        avg = sum(wagons)//len(wagons)
        ans = 0
        ind=0
        for i in wagons:
            if abs(i - avg) < abs(wagons[ans]-avg):
                ans = ind
            ind +=1
        wagons.pop(ans)
    curr=input()
wagons.reverse()
print(' '.join([str(i) for i in wagons+[pow]]))