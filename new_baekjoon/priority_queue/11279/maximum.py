import sys
import heapq

input=sys.stdin.readline

n=int(input())

heap=[]

for _ in range(n):
    num=int(input())
    if not num:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-num,num))

"""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""