n = int(input())
if n>= 1:
    Max = int(input())
    for i in range(1,n):
        current_number = int(input())
        Max = max (Max, current_number)
    print(Max)