def bubble_sort(list):
    swapped=True
    while swapped:
        swapped = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                curr = list[i]
                list[i] = list[i+1]
                list[i+1] = curr
                swapped = True
nums = [int(item) for item in input().split(' ')]
bubble_sort(nums)
for i in range(len(nums)):
    nums[i]=str(nums[i])
print(' '.join(nums))