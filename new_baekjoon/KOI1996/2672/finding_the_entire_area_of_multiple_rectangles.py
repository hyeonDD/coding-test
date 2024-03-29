import sys
input = sys.stdin.readline

def count(list):
    cnt = 0
    for e in list:
        if e != 0:
            cnt += 1
    return cnt

n = int(input())
rec = []
for _ in range(n):
    x, y, w, h = map(float, input().split())
    rec.append([x, y, y+h, True])
    rec.append([x+w, y, y+h, False])

rec.sort()

area = 0
ylist = [0]*25001

for i in range(len(rec)-1):
    x, y1, y2, flag = rec[i]
    y1 = int(y1*10)
    y2 = int(y2*10)
    if flag:
        for j in range(y1, y2):
            ylist[j] += 1
    if not flag:
        for j in range(y1, y2):
            ylist[j] -= 1
    area += (rec[i+1][0] - x)*count(ylist)/10

if area-int(area) > 0:
    print(f'{area:0.2f}')
else:
    print(int(area))