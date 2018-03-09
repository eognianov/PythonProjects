magic=int(input())
for _1 in range(1,10):
    if magic % _1 != 0:
        continue
    for _2 in range(1,10):
        if magic % _2 != 0:
            continue
        for _3 in range(1, 10):
            if magic % _3 != 0:
                continue
            for _4 in range(1, 10):
                if magic % _4 != 0:
                    continue
                print('{}{}{}{} '.format(_1,_2,_3,_4),end='')