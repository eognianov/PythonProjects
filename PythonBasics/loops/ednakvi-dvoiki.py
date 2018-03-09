n =int(input())
curr_pair_sum=0
prev_pair_sum=0
max_diff_pair=0
for i in range (2*n):
    curr = int(input())
    curr_pair_sum += curr
    if i % 2 == 0 and i>=4:
        max_diff_pair=max(max_diff_pair,abs(curr_pair_sum - prev_pair_sum))
    if i % 2 == and i >=2:
        prev_pair_sum = curr_pair_sum
        curr_pair_sum = 0

