tel = list(map(int,input().split(' ')))
#tel = [int(x) for x in input().split(' ')]
current_index, answer = 0, 0

while current_index!=len(tel):
    if tel[current_index]==0:
        answer+=1
        current_index+=1
    else:
        old_index = current_index
        current_index = tel[current_index]
        tel[old_index]=0
print(answer)