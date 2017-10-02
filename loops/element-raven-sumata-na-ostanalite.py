n = int(input())
Sum = 0
Max =int(input())
Sum += Max
for i in range(1,n):
    curr=int(input())
    Sum += curr
    Max = max(Max,curr)
if Max == (Sum - Max):
    print('Yes\nSum = {0}'.format(Max))
else:
    print('No\Diff = {0}'.format(abs(Max - (Sum-Max))))