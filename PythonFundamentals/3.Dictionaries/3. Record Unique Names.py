n = int(input())
S=set()
ans=list()
for i in range(n):
    name=input()
    if name in S:
        continue
    else:
        S.add(name)
        ans.append(name)
for x in ans:
    print(x)