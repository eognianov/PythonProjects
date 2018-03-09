n = int(input())
prev=1
curr=1
for i in range(2,n+1):
    next=prev+curr
    prev=curr
    curr=next
print(curr)