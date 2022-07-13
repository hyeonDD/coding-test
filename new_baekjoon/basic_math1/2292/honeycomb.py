import sys

n = int(sys.stdin.readline())

cnt = 1

while n>0:
    if n ==1:
        break
    n = n -6*cnt
    cnt+=1

print(cnt)
