n = int(input())
even_sum = 0
even_min = 1000000000.0
even_max = -1000000000.0
odd_sum = 0
odd_min = 1000000000.0
odd_max = -1000000000.0
for i in range(1,n+1):
    curr = float(input())
    if (i%2 == 0):
        even_sum += curr
        even_max = max(even_max, curr)
        even_min = min(even_min, curr)
    else:
        odd_sum += curr
        odd_max = max(odd_max, curr)
        odd_min = min(odd_min, curr)
if odd_min == 1000000000.0:
    odd_min='no'
if even_min == 1000000000.0:
    even_min='no'
if odd_max == -1000000000.0:
    odd_max='no'
if even_max == -1000000000.0:
    even_max='no'
print('OddSum={0}, OddMin={1}, OddMax={2}, EvenSum={3}, EvenMin={4}, EvenMax={5}'.format(odd_sum,odd_min,odd_max,even_sum,even_min,even_max))