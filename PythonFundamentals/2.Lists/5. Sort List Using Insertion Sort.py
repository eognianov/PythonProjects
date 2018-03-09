def insertion_sort(list):
   lastSorted = 0
   while lastSorted != len(list)-1:
       currentIndex=lastSorted
       while currentIndex>=0 and list[currentIndex]>list[lastSorted+1]:
           currentIndex-=1
       currentElement=list[lastSorted+1]
       list.pop(lastSorted+1)
       list.insert(currentIndex+1,currentElement)
       lastSorted+=1


nums = [int(item) for item in input().split(' ')]
insertion_sort(nums)
for i in range(len(nums)):
    nums[i]=str(nums[i])
print(' '.join(nums))