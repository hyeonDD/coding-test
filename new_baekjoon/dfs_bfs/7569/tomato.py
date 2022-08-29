import sys
from collections import deque

input=sys.stdin.readline

m,n,h=map(int,input().split())

graph=[[[*map(int,input().split())] for _ in range(n)] for _ in range(h)]

# pprint(graph)

q=deque()
for i in range(h):
    for j in range(n):
        for ij in range(m):
            if graph[i][j][ij]==1:
                q.append((i,j,ij))

# print(q)

direction=[(1,0,0),(-1,0,0),(0,0,-1),(0,0,1),(0,-1,0),(0,1,0)]# 상 하 좌 우 #같은층 상 하
# direction=[,]

while q:
    x,y,z=q.popleft()

    for nx,ny,nz in direction:
        nx+=x
        ny+=y
        nz+=z
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz]==0:
            graph[nx][ny][nz]=graph[x][y][z]+1
            q.append((nx,ny,nz))

# pprint(graph)

result=0
for grap in graph:
    for g in grap:
        if 0 in g:
            print(-1)
            sys.exit(0)
        result=max(result,max(g))
print(result-1)