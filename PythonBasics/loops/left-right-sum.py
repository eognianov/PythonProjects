n = int(input())
if n==0:
    print('I don`t know')
else:
    left_sum, right_sum = 0, 0
    for i in range(n):
        left_sum += int(input())
    for i in range(n):
        right_sum += int(input())
    if left_sum == right_sum:
        print("Yes, sum = {0}".format(left_sum))
    else:
        print("No, diff = {0}".format(abs(right_sum-left_sum)))