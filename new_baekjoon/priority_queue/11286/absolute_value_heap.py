import heapq
import sys

input=sys.stdin.readline

n=int(input())

q=[]

for _ in range(n):
    num=int(input())
    
    if not num:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q,(abs(num),num))
"""
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
"""