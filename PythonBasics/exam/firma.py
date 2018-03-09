need = int(input())
days = int(input())
hardworking = int(input())

time = int(days * 9 * 8/10) + hardworking*2*days

if time >= need:
    print('Yes!{0} hours left.'.format(time-need))
else:
    print('Not enough time!{0} hours needed.'.format(need-time))