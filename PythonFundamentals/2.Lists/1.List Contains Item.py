def find(list,item):
    for i in list:
        if item == i:
            return True
    return False
nums = [int(item) for item in input().split(' ')]
searchFor = int(input())
print('yes' if find(nums,searchFor) else 'no')