n = int(input())
if n>= 1:
    Min = int(input())
    for i in range(1,n):
        current_number = int(input())
        Min = min(Min, current_number)
    print(Min)