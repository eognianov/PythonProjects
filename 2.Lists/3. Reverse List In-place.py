def reverse_list(list):
    for i in range(len(list)//2):
        curr=list[i]
        list[i]=list[-i-1]
        list[-i-1]=curr

nums = [int(item) for item in input().split(' ')]
reverse_list(nums)
for i in nums:
    print(i, end=' ')