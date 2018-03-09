n = int(input())
widthSide = n//2
widthMidd = n
print('/' + '^' * (widthSide) + '\\' + '_' * (2 * n - 4 - 2 * widthSide) + '/' + '^' * (widthSide) + '\\')
for i in range(n-3):
    print('|' + ' '*(2*n-2)+'|')
print('|'+ ' ' * (widthSide+1)+'_'*(2 * n - 4 - 2 * widthSide)+ ' ' * (widthSide+1)+'|' )
print('\\' + '_' * (widthSide) + '/' + ' ' * (2 * n - 4 - 2 * widthSide) + '\\' + '_' * (widthSide) + '/')
