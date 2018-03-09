tel = list(map(int,input().split(' ')))
#tel = [int(x) for x in input().split(' ')]
current_index, answer = 0, 0

while current_index!=len(tel):
    answer += int(tel[current_index]==0)
    tel[current_index],current_index = 0, (current_index+1 if tel[current_index]==0 else tel[current_index] )
print(answer)