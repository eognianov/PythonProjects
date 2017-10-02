n = int(input())
print('.'*(n+1)+ '_'*(2*n+1)+'.'*(n+1))
for i in range(n):
    print('.'*(n-i) + '//' + "_"*(2*n-1+2*i)+'\\\\'+'.'*(n-i))
print('//'+'_'*(2*n-3)+'STOP!'+'_'*(2*n-3)+'\\\\')
for i in range(n):
    print('.'* i + '\\\\'+'_'*(4*n-1-2*i)+'//'+'.'*i)