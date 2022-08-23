import sys
from collections import deque

input=sys.stdin.readline

n,m,r=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i]=reversed(sorted(graph[i]))

visited=[0]*(n+1)

q=deque([])
cnt=1

def bfs(v):
    global cnt
    q.append(v)
    visited[v]=cnt

    while q:
        t=q.popleft()

        for g in graph[t]:
            if not visited[g]:
                cnt+=1
                visited[g]=cnt
                q.append(g)

bfs(r)

for i in visited[1:]:
    print(i)

