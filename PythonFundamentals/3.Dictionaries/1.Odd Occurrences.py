line = input().lower()
words = line.split(' ')
counts={}
print_order = list()
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
        print_order.append(word)
results=[]
for key in print_order:
    value=counts[key]
    if value % 2 ==1:
        results.append(key)
print(', '.join(results))