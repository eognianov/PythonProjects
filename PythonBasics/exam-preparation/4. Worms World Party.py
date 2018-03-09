line = input()

teams = dict()
all_members = set()
while line != 'quit':
    line = line.split('->')
    name, team, score = line[0],line[1],line[2]
    if not (name in all_members):
        if team in teams:
            teams[team][name] = score
        else:
            teams[team]={name:score}
        all_members.add(name)
    line = input()
count = 1
#printscreen