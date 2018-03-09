n = int(input())
for i in range(2*(n-2)+1):
    if i < n-2:
        if i % 2 == 0:
            print('*'*(n-2)+'\\ /'+'*'*(n-2))
        else:
            print('-' * (n - 2) + '\\ /' + '-' * (n - 2))
    elif i == n-2:
        print(' ' * (n - 2) + ' @ ' + ' ' * (n - 2))
    else:
        if i % 2 == 0:
            print('*' * (n - 2) + '/ \\' + '*' * (n - 2))
        else:
            print('-' * (n - 2) + '/ \\' + '-' * (n - 2))