import re

curr = input()
while curr != 'Traincode':
    if re.search(r'^(<\[[^A-Za-z0-9]*?\]\.)+(\.\[[A-Za-z0-9]*\]\.)*$', curr) != None:
        print(curr)
    curr = input()