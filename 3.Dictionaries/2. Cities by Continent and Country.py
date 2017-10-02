n = int(input())
continets={}
for i in range(n):
    strs = input().split(' ')
    if strs[0] in continets:
        if strs[1] in continets[strs[0]]:
            continets[strs[0]][strs[1]].append([strs[2]])
        else:
            continets[strs[0]][strs[1]]=[strs[2]]
    else:
        continets[strs[0]]={
            strs[1]:[strs[2]]
        }
print(continets)