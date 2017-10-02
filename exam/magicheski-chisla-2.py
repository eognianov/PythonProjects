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
                for _5 in range(1, 10):
                    if magic % _5 != 0:
                        continue
                    for _6 in range(1, 10):
                        if magic % _6 != 0:
                            continue
                        if _1*_2*_3*_4*_5*_6==magic:
                            print('{}{}{}{}{}{} '.format(_1,_2,_3,_4,_5,_6),end='')