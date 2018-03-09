inp = input()
trains = []
while inp != 'It’s Training Men!':
    inp = inp.split(' ')
    if inp[1] == '->' and len(inp)==5:
        ex = False
        for i in range(len(trains)):
            name,wagons = trains[i]
            if name == inp[0]:
                ex = True
                wagons+=[(inp[2],inp[4])]
                trains[i]=(name,wagons)
                break
        if not ex:
            trains+=[(inp[0],[(inp[2],inp[4])])]
    elif inp[1] == '->' and len(inp) == 3:
        ind1 = -1
        ind2 = -1
        for i in range(len(trains)):
            name,wagons = trains[i]
            if name == inp[0]:
                ind1 = i
            if name == inp[2]:
                ind2 = i
        t1n,t1w = trains[ind1]
        t2n,t2w = trains[ind2]
        trains[ind1] = (t1n,t1w+t2w)
        trains[ind2] = (t2n,[])
    else:
        ind1 = -1
        ind2 = -1
        for i in range(len(trains)):
            name, wagons = trains[i]
            if name == inp[0]:
                ind1 = i
            if name == inp[2]:
                ind2 = i
        t1n, t1w = trains[ind1]
        t2n, t2w = trains[ind2]
        trains[ind1] = (t1n, t1w + t2w)
    inp=input()

print(trains)