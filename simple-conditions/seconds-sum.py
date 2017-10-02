a = int(input())
b = int(input())
c = int(input())

sum = a + b + c

if sum < 60:
    min = 0
    sec = sum

else:
    min = sum // 60
    sec = sum % 60

if sec < 10:
    print(str(min) + ':0' + str(sec))
else:
    print(str(min) + ':' + str(sec))
