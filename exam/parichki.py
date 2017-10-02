BC = int(input())
CU = float(input())
COM = float(input())

LVBC = BC * 1168
DOCU = CU * (15/100)
LVDO = DOCU * (176/100)
EUR = (LVBC + LVDO)*100 / 195
res = EUR - EUR*COM/100
print('{0:.2f}'.format(res))