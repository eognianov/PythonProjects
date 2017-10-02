free = int(input())
not_free = 365-free
play=free *127+not_free*63
if (play<30000):
    print('Tom sleeps well\n{0} hours and {1} minutes less for play'.format((30000-play)//60,(30000-play)%60))
else:
    print('Tom will run away\n{0} hours and {1} minutes more for play'.format(abs(30000-play)//60,abs(30000-play)%60))