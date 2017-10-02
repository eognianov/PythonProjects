def insertion_sort(list):
   result = list[:1]
   list.pop(0)
   while len(list)!=0:
       current_index=len(result)-1
       while current_index>=0 and list[0]<result[current_index]:
           current_index-=1
       result.insert(current_index+1,list[0])
       list.pop(0)
   return result
nums = [int(item) for item in input().split(' ')]
nums=insertion_sort(nums)
for i in range(len(nums)):
    nums[i]=str(nums[i])
print(' '.join(nums))