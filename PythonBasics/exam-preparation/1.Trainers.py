n = int(input())

teams = {"Theoretical":0.0,"Technical":0.0,"Practical":0.0}

for i in range(n):
    dist = float(input())
    cargo = float(input())
    team = input()
    try:
        teams[team] += (cargo*100*15) - (7 *dist*16*25)
    except:
        teams[team] = (cargo * 100 * 15) - (7 * dist * 16 * 25)
max = None
ans = None
for k,v in teams.items():
    if max==None or ans==None or max < v:
        max = v
        ans = k
print ('The {0} Trainers win with ${1:.3f}.'.format(ans,max))