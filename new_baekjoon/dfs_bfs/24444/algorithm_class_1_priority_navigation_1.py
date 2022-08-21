from collections import deque
import sys

input=sys.stdin.readline

n,m,r=map(int,input().split())

# graph=deque([[] for _ in range(n+1)])
graph=[[] for _ in range(n+1)]

visited=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

cnt=1
q=deque([])

def bfs(v):
    global cnt
    q.append(v)
    visited[v]=1
    while q:
        v=q.popleft()
        for g in graph[v]:
            if not visited[g]:
                cnt+=1
                visited[g]=cnt
                q.append(g)

bfs(r)
for i in visited[1:]:
    print(i)