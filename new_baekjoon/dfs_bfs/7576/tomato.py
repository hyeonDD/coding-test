import sys
from collections import deque

input=sys.stdin.readline

m,n=map(int,input().split())

graph=[]
q=deque()
for i in range(n):
    tmp=list(map(int,input().split()))
    
    tmp2=0
    cnt=tmp.count(1)
    for j in range(cnt):
        idx=tmp.index(1,tmp2)
        tmp2=idx+1
        q.append((i,idx))
    graph.append(tmp)

direction=[(1,0),(-1,0),(0,-1),(0,1)]

while q:
    x,y=q.popleft()

    for nx,ny in direction:
        nx+=x
        ny+=y
        # print(nx,ny)
        if (-1<nx<n and -1<ny<m and graph[nx][ny]==0):
            graph[nx][ny]=graph[x][y]+1
            q.append((nx,ny))

cnt=0

for g in graph:
    if 0 in g:
        print(-1)
        sys.exit(0)
    cnt=max(cnt,max(g))
print(cnt-1)