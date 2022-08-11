import sys

input=sys.stdin.readline

table=[[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            table[x][y]=1
total=0
for i in table:
    total+=sum(i)
print(total)
