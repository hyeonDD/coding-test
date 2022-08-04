import heapq
import sys

input=sys.stdin.readline

n=int(input())

min_q=[]
max_q=[]

for _ in range(n):
    num=int(input())

    if len(min_q)==len(max_q):
        heapq.heappush(max_q,-num)
    else:
        heapq.heappush(min_q,num)
    if min_q and -max_q[0]>min_q[0]:
        max_value=heapq.heappop(max_q)
        min_value=heapq.heappop(min_q)

        heapq.heappush(max_q,-min_value)
        heapq.heappush(min_q,-max_value)
    
    print(-max_q[0])