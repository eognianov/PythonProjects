masiv = input()
items=masiv.split(' ')
nums = []
for i in items:
    nums+=[int(i)]
min = nums[0]
for i in range(len(nums)):
    if nums[i]<min:
        min = nums[i]
print(min)