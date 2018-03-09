n = int(input())
num = 1
num_by_line = 1
while True:
    for i in range(num_by_line):
        print(num, end=' ')
        num+=1
        if num>n:
            break
    if num>n:
        break
    num_by_line +=1
    print()