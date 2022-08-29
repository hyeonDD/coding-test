import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())

graph=[0]*101
visited=[False]*101

ladder=dict()
snack=dict()

for _ in range(n):
    a,b=map(int,input().split())
    ladder[a]=b

for _ in range(m):
    a,b=map(int,input().split())
    snack[a]=b

def bfs():
    q=deque([1])
    while q:
        x=q.popleft()
        for nx in range(1,7):
            nx+=x
            if 0<nx<101 and not visited[nx]:
                if nx in ladder.keys():
                    nx = ladder[nx]
                
                if nx in snack.keys():
                    nx = snack[nx]

                if not visited[nx]:
                    q.append(nx)
                    visited[nx]=True
                    graph[nx]=graph[x]+1
    return graph[100]

print(bfs())

print(graph)