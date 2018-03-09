nums =list(float(x) for x in input().split(' '))
#nums = map(float,input().split(' '))
#nums=[]
#for x in input().split(' '):
#    nums.append(float(x))
count={}
for x in nums:
    if x in count:
        count[x]+=1
    else:
        count[x]=1
for num in sorted(count):
    print('{} -> {}'.format((num if num!=int(num) else int(num)), count[num]))