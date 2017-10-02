def print_header_row(n):
    print('-' * 2 * n)
def print_middle_row(n):
    print('-', end='')
    for i in range(n-1):
        print('\\/', end='')
    print('-')
n = int(input())
print_header_row(n)
for i in range(n-2):
    print_middle_row(n)
print_header_row(n)