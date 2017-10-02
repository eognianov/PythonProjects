masiv = input()
items=masiv.split(' ')
nums = []
p=float(input())
for i in items:
    nums+=[float(i)*p]
for i in nums:
    print(i, end=' ')