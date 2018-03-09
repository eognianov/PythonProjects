def print_line(start,end):
    for i in range(start,end+1):
        print(i, end=' ')
def print_triangle(n):
    for i in range(1,n):
        print_line(1,i)
        print()
    for i in range(n, 0, -1):
        print_line(1,i)
        print()
n = int(input())
print_triangle(n)