n = int(input())
studentbook={}
students_in_order=[]
def my_str(x):
    return '{:.2f}'.format(x)
for i in range(n):
    line = input().split(' ')
    name, mark = line[0],float(line[1])
    if name in studentbook:
        studentbook[name].append(mark)
    else:
        studentbook[name]=[mark]
        students_in_order.append(name)
for name in students_in_order:
    print('{} -> '.format(name),end='')
    print(' '.join(map(my_str,studentbook[name])),end='')
    print(' (avg: {:.2f})'.format(sum(studentbook[name])/len(studentbook[name])))