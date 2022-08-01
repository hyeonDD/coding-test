import heapq
import sys

input=sys.stdin.readline

q=[]

n=int(input())

for _ in range(n):
    num=int(input())

    if not num:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q,(num,num))