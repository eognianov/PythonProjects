n = int(input())
if n==0:
    print('Yes\nSum = 0')
else:
    odd_sum, even_sum = 0, 0
    for i in range(n):
       if i % 2 == 0:
           even_sum +=int(input())
       else:
           odd_sum += int(input())
    if odd_sum == even_sum:
        print("Yes,\nSum = {0}".format(odd_sum))
    else:
        print("No,\nDiff = {0}".format(abs(even_sum)))