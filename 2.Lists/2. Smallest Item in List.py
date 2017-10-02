def find_min(list):
    curr = list[0]
    for i in list[1:]:
        if curr > i:
            curr=i
    return curr
nums = [int(item) for item in input().split(' ')]
print(find_min(nums))